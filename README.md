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

#`accelerometer_landing_to_trusted.py` - a python script using Spark that sanitizes Accelerometer data from the Mobile App (Landing Zone) - and only stores Accelerometer Reading from customers who agreed to share their data for research purposes (Trusted Zone) - creating a glue table called accelerometer_trusted.
