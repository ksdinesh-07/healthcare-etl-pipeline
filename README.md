# Healthcare ETL Pipeline

## Project Overview
An automated ETL pipeline that processes daily healthcare visit data, transforms it, and loads it into Amazon Redshift for analytics with SNS notifications.

## Dataset Structure
- **Dimension Tables**: patients, doctors, departments, diagnoses (4 CSV files)
- **Fact Tables**: Daily patient visits (30 CSV files)

## Technologies
- AWS S3, Glue, Step Functions, EventBridge, Redshift, SNS
- Python, Pandas, PySpark

## Author
Dinesh K
