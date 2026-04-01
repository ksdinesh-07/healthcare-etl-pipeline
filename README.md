# 🏥 Healthcare ETL Pipeline on AWS

## 📌 Project Overview

This project demonstrates a **fully automated, end-to-end ETL pipeline** built on AWS to process healthcare data. The pipeline ingests CSV files from S3, transforms and enriches the data using AWS Glue, and loads it into Amazon Redshift for analytics. It is designed using **event-driven architecture**, **workflow orchestration**, and **infrastructure as code (IaC)**.

---

## 🚀 Key Features

* ✅ Fully automated ETL pipeline
* ✅ Event-driven processing using EventBridge
* ✅ Workflow orchestration with Step Functions
* ✅ Schema discovery using Glue Crawlers
* ✅ Data transformation using Glue (PySpark)
* ✅ Data warehousing using Redshift Serverless
* ✅ Email notifications using SNS
* ✅ Infrastructure as Code (CloudFormation & Terraform)
* ✅ CI/CD pipeline using GitHub Actions

---

## 🏗️ Architecture Overview

### 🔹 Data Flow

1. **Data Ingestion**

   * CSV files uploaded to S3 (`dim/` and `daily-visits/` folders)

2. **Event Trigger**

   * EventBridge detects new file upload and triggers Step Functions

3. **Schema Discovery**

   * Glue Crawlers scan data and update Glue Data Catalog

4. **Data Transformation**

   * Glue ETL job processes and enriches data

5. **Data Loading**

   * Transformed data is loaded into Redshift Serverless

6. **Notification**

   * SNS sends success/failure email alerts

7. **Monitoring**

   * CloudWatch logs track pipeline execution

---

## 📂 Project Structure

```
healthcare-etl-pipeline/
│
├── .github/workflows/
│   └── deploy.yml
│
├── cloudformation/
│   └── complete-stack.yaml
│
├── data/
│   ├── dim/
│   │   ├── patients.csv
│   │   ├── doctors.csv
│   │   ├── departments.csv
│   │   └── diagnoses.csv
│   │
│   └── daily-visits/
│       ├── visits_20240101.csv
│       ├── visits_20240102.csv
│       ├── visits_20240103.csv
│       ├── visits_20240104.csv
│       └── visits_20240105.csv
│
├── glue-scripts/
│   └── healthcare-etl-job.py
│
├── step-functions/
│   └── state-machine.json
│
├── eventbridge/
│   └── rule.json
│
├── lambda-functions/
│   └── redshift-loader.py
│
├── scripts/
│   ├── deploy.sh
│   ├── test-pipeline.sh
│   └── setup-local.sh
│
├── terraform/
│   └── main.tf
│
├── docs/
│   └── architecture.md
│
├── README.md
└── .gitignore
```

---

## ⚙️ AWS Services Used

| Service             | Purpose                |
| ------------------- | ---------------------- |
| S3                  | Data lake storage      |
| EventBridge         | Event-driven triggers  |
| Step Functions      | Workflow orchestration |
| Glue Crawler        | Schema discovery       |
| Glue ETL            | Data transformation    |
| Redshift Serverless | Data warehouse         |
| SNS                 | Email notifications    |
| Lambda              | Redshift data loading  |
| CloudFormation      | Infrastructure as Code |
| Terraform           | Alternative IaC        |
| GitHub Actions      | CI/CD pipeline         |

---

## 🔄 Step Function Workflow

The pipeline follows this sequence:

1. Start Dimension Crawler
2. Wait & Check Status
3. Start Fact Crawler
4. Wait & Check Status
5. Start Glue Job
6. Monitor Job Execution
7. Send Success/Failure Notification

---

## 🧪 Sample Analytics Queries

### 📊 Daily Visit Trends

```sql
SELECT visit_date, COUNT(*) as total_visits, AVG(treatment_cost) as avg_cost
FROM healthcare.visits
GROUP BY visit_date
ORDER BY visit_date DESC;
```

### 💰 Top Expensive Treatments

```sql
SELECT d.diagnosis_name, AVG(v.treatment_cost) as avg_cost
FROM healthcare.visits v
JOIN healthcare.diagnoses d 
ON v.diagnosis_code = d.diagnosis_code
GROUP BY d.diagnosis_name
ORDER BY avg_cost DESC
LIMIT 5;
```

### 🏥 Department Workload

```sql
SELECT dep.department_name, COUNT(*) as total_visits
FROM healthcare.visits v
JOIN healthcare.departments dep 
ON v.department_id = dep.department_id
GROUP BY dep.department_name;
```

---

## 💡 Cost Optimization

* Redshift Serverless auto-pauses when idle
* Minimal Glue workers (G.1X) used
* S3 lifecycle policy moves old data to Glacier
* Crawlers run only when needed
* AWS Free Tier leveraged where possible

---

## ▶️ How to Deploy

### Option 1: Using CloudFormation

```bash
aws cloudformation deploy \
  --template-file cloudformation/complete-stack.yaml \
  --stack-name healthcare-etl-stack
```

### Option 2: Using Terraform

```bash
cd terraform
terraform init
terraform apply
```

### Option 3: CI/CD (GitHub Actions)

* Push code to repository
* Workflow auto-deploys infrastructure

---

## 🧪 Testing the Pipeline

```bash
bash scripts/test-pipeline.sh
```

Upload a new file to:

```
s3://<your-bucket>/daily-visits/
```

This will trigger the entire pipeline automatically.

---

## 📬 Notifications

* SNS sends email alerts for:

  * ✅ Successful pipeline execution
  * ❌ Failure with error details

---

## 📈 Future Enhancements

* Add real-time streaming (Kinesis)
* Implement data quality checks
* Add dashboard (QuickSight/Power BI)
* Partition optimization in Redshift
* Incremental data loading

---

## 👨‍💻 Author

**Dinesh K**
📧 [ks.dinesh005@gmail.com](mailto:ks.dinesh005@gmail.com)

---

## 🎉 Conclusion

This project demonstrates a **production-ready ETL pipeline** with:

* Scalable architecture
* Automation and orchestration
* Robust error handling
* CI/CD integration
* Cost-efficient design

It showcases real-world AWS data engineering practices and is ready for enterprise-level deployment.

---

⭐ If you like this project, feel free to star the repository!
