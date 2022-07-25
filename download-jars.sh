#! /bin/bash

python=$1

# Jars for accessing AWS S3 : s3a filesystem
wget --no-verbose https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/hadoop-aws-3.3.2.jar -P venv/lib64/${python}/site-packages/pyspark/jars/
wget --no-verbose https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1026/aws-java-sdk-bundle-1.11.1026.jar -P venv/lib64/${python}/site-packages/pyspark/jars/
wget --no-verbose https://repo1.maven.org/maven2/org/apache/spark/spark-avro_2.12/3.3.0/spark-avro_2.12-3.3.0.jar -P venv/lib64/${python}/site-packages/pyspark/jars/