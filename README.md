# Crypto Data Engineering Pipeline

An end-to-end data engineering pipeline that automatically extracts cryptocurrency market data, stores and processes it locally, loads it into AWS, and exposes the data for analytics and visualization.

## Architecture

```text
Crypto Market API
       ↓
    Python
       ↓
  PostgreSQL
       ↓
 Apache Airflow
       ↓
    AWS S3
       ↓
Amazon Redshift Serverless
       ↓
      SQL
       ↓
Amazon QuickSight
       ↓
Analytics Dashboard
```

## Tech Stack

- Python
- PostgreSQL
- Apache Airflow
- Docker / Docker Compose
- AWS S3
- Amazon Redshift Serverless
- Amazon QuickSight
- SQL
- Git / GitHub

## Pipeline

The pipeline is orchestrated by Apache Airflow and runs the following tasks sequentially:

```text
run_crypto_pipeline
        ↓
export_to_s3
        ↓
load_to_redshift
```

### 1. Extract and Load

Python retrieves hourly cryptocurrency OHLCV market data from a REST API.

The data contains:

- timestamp
- open price
- high price
- low price
- close price
- trading volume

The records are loaded into PostgreSQL. Duplicate timestamps are prevented during ingestion.

### 2. Export to Amazon S3

Airflow exports the PostgreSQL data to CSV and uploads the resulting object to an Amazon S3 bucket.

S3 acts as the cloud storage layer between the operational database and the analytical data warehouse.

### 3. Load into Amazon Redshift

The pipeline automatically loads the S3 dataset into Amazon Redshift Serverless.

Redshift provides the analytical warehouse used for SQL queries and downstream business intelligence.

### 4. Analytics

SQL queries are used to calculate metrics including:

- average closing price
- daily high and low prices
- trading volume
- historical price trends

### 5. Visualization

Amazon QuickSight connects to Redshift and provides an interactive analytics dashboard containing:

- Bitcoin price over time
- trading volume over time
- daily high vs. low price
- average Bitcoin price
- maximum Bitcoin price
- total trading volume

## Project Structure

```text
crypto_pipeline/
├── dags/
│   └── crypto_pipeline_dag.py
├── src/
│   ├── extract.py
│   ├── load.py
│   ├── export.py
│   └── redshift.py
├── sql/
│   └── create_tables.sql
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Running the Project

Start the Docker services:

```bash
docker compose up -d
```

Check their status:

```bash
docker compose ps
```

Airflow is available locally at:

```text
http://localhost:8080
```

The `crypto_pipeline` DAG orchestrates the complete workflow.

## Configuration and Security

Database credentials are passed to the application through environment variables rather than being hardcoded in the Python source code.

AWS authentication is handled through AWS credentials available to the Airflow environment.

IAM permissions are configured for the required S3 and Redshift operations.

Sensitive credentials and generated Python files are excluded from version control.

## Data Engineering Concepts Demonstrated

This project demonstrates:

- REST API data ingestion
- relational database storage
- workflow orchestration
- containerized services
- cloud object storage
- data warehouse loading
- IAM-based AWS access
- SQL analytics
- BI dashboard development
- automated end-to-end data pipelines

## Future Improvements

Possible extensions include:

- incremental S3 and Redshift loading
- data quality checks
- Airflow retries and alerting
- automated QuickSight dataset refresh
- infrastructure as code
- CI/CD
- partitioned cloud storage
- larger historical datasets