import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1687233090721 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi_lakehouse",
    table_name="step_trainer_trusted",
    transformation_ctx="StepTrainerTrusted_node1687233090721",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi_lakehouse",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1",
)

# Script generated for node Trusted Zone Join at Timestamp
TrustedZoneJoinatTimestamp_node1687233125453 = Join.apply(
    frame1=AccelerometerTrusted_node1,
    frame2=StepTrainerTrusted_node1687233090721,
    keys1=["timestamp"],
    keys2=["sensorreadingtime"],
    transformation_ctx="TrustedZoneJoinatTimestamp_node1687233125453",
)

# Script generated for node Drop Duplicate TImestamp
DropDuplicateTImestamp_node1687233181775 = DropFields.apply(
    frame=TrustedZoneJoinatTimestamp_node1687233125453,
    paths=["sensorreadingtime"],
    transformation_ctx="DropDuplicateTImestamp_node1687233181775",
)

# Script generated for node Combined Accelerometer and Step Trainer Trusted
CombinedAccelerometerandStepTrainerTrusted_node3 = (
    glueContext.write_dynamic_frame.from_options(
        frame=DropDuplicateTImestamp_node1687233181775,
        connection_type="s3",
        format="json",
        connection_options={
            "path": "s3://stedi-lakes-analytics/step_trainer/machine_learning_curated/",
            "partitionKeys": [],
        },
        transformation_ctx="CombinedAccelerometerandStepTrainerTrusted_node3",
    )
)

job.commit()
