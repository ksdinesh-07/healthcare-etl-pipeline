import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, current_timestamp, lit

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_BUCKET', 'PROCESS_DATE'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_bucket = args['S3_BUCKET']

# Read dimension tables
patients_df = spark.read.option("header", "true").csv(f"s3://{s3_bucket}/dim/patients.csv")
doctors_df = spark.read.option("header", "true").csv(f"s3://{s3_bucket}/dim/doctors.csv")

# Read fact table
visits_df = spark.read.option("header", "true").csv(f"s3://{s3_bucket}/daily-visits/")

# Enrich data
enriched_df = visits_df \
    .join(patients_df, "patient_id", "left") \
    .join(doctors_df, "doctor_id", "left") \
    .withColumn("load_timestamp", current_timestamp()) \
    .withColumn("source_system", lit("S3_HEALTHCARE"))

print(f"Processed {enriched_df.count()} records")

job.commit()
