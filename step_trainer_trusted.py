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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lakes-analytics/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerLanding_node1",
)

# Script generated for node Customer Curated with Accelerometer Data
CustomerCuratedwithAccelerometerData_node1687230694385 = (
    glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": False},
        connection_type="s3",
        format="json",
        connection_options={
            "paths": ["s3://stedi-lakes-analytics/customer/curated/"],
            "recurse": True,
        },
        transformation_ctx="CustomerCuratedwithAccelerometerData_node1687230694385",
    )
)

# Script generated for node Privacy Filter Zone
PrivacyFilterZone_node1687230845320 = Join.apply(
    frame1=StepTrainerLanding_node1,
    frame2=CustomerCuratedwithAccelerometerData_node1687230694385,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="PrivacyFilterZone_node1687230845320",
)

# Script generated for node Curated Step Trainer Data
CuratedStepTrainerData_node1687230897103 = DropFields.apply(
    frame=PrivacyFilterZone_node1687230845320,
    paths=[
        "birthDay",
        "timeStamp",
        "shareWithPublicAsOfDate",
        "shareWithResearchAsOfDate",
        "registrationDate",
        "customerName",
        "lastUpdateDate",
        "email",
        "phone",
        "shareWithFriendsAsOfDate",
    ],
    transformation_ctx="CuratedStepTrainerData_node1687230897103",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=CuratedStepTrainerData_node1687230897103,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lakes-analytics/step_trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="StepTrainerTrusted_node3",
)

job.commit()
