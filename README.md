# UdacityProject3_STEDI-Analytics

## PROJECT Overview

The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

    trains the user to do a STEDI balance exercise;
    and has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
    has a companion mobile app that collects customer data and interacts with the device sensors.

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

## Files included:

#`customer_landing_to_trusted.py` - a python script using Spark that sanitizes the Customer data from the website (landing zone) and only stores the Records who agreed to share their data for research purposed (Trusted Zone) - creating a Glue Table called customer_trusted. (screenshot - `customer_trusted.png`) 

#`accelerometer_landing_to_trusted_zone.py` - a python script using Spark that sanitizes Accelerometer data from the Mobile App (Landing Zone) - and only stores Accelerometer Reading from customers who agreed to share their data for research purposes (Trusted Zone) - creating a glue table called accelerometer_trusted.

#`customer_curated.py` - a python script using Spark that sanitizes the Customer data (Trusted Zone) and creates a Glue Table (Curated Zone) that only includes customers who have accelerometeter data and have agreed to share their data for research. 

#`step_trainer_trusted.py` - a python script using Spark that reads the Step Trianer IoT data stream (S3) and populated a Trusted Zone Glue Table called step_trainer_trusted containing the Step Trainer records data for customers who have accelerometer data and have agreed to share their data for research (customer_curated).

#`machine_learning_curated.py` - a python script that creates an aggregated table that has each of the Step Trainer readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data, and populates a glue table (machine_learning_curated).

#`customer_landing.sql` and `accelerometer_landing.sql` - SQL DDL scripts from Athena query editor of landing folders from raw data.

#`customer_landing.png`, `accelerometer_landing.png` and ` customer_trusted.png` - output of tables for customer landing, accelerometer landing and customer trusted zone tables.
