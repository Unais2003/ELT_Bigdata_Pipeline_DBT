# NYC Taxi ELT Pipeline with dbt + DuckDB

## Project Overview

This project demonstrates a modern ELT (Extract, Load, Transform) analytics engineering workflow using:

- dbt
- DuckDB
- SQL
- Parquet files

The project processes NYC Yellow Taxi trip data and transforms raw trip records into analytics-ready business models using layered dbt transformations.

Originally, the project was implemented as a Spark-based ETL pipeline. The transformation logic was later adapted into a warehouse-native ELT architecture inspired by modern analytics engineering workflows using dbt and BigQuery concepts.

---

# Architecture

```text
Raw Parquet Files
        ↓
Staging Models
        ↓
Intermediate Feature Models
        ↓
Mart / Analytics Models
        ↓
Business Reporting
```

---

# Tech Stack

| Component | Technology |
|---|---|
| Transformation Framework | dbt |
| Local Warehouse Engine | DuckDB |
| Data Format | Parquet |
| Language | SQL |
| Original Pipeline | PySpark |
| Warehouse Concept | BigQuery-style ELT |

---

# Project Structure

```text
ELT_nyc_taxi_dbt/
│
├── models/
│   ├── staging/
│   ├── intermediate/
│   ├── marts/
│   └── sources.yml
│
├── data/raw/
├── tests/
├── macros/
├── analyses/
├── snapshots/
│
├── dbt_project.yml
├── profiles.yml
├── README.md
└── .gitignore
```

---

# Data Schema

Main taxi trip columns:

- vendorid
- passenger_count
- trip_distance
- payment_type
- fare_amount
- tip_amount
- total_amount
- tpep_pickup_datetime
- tpep_dropoff_datetime
- pulocationid
- dolocationid

---

# ELT Layers

## 1. Staging Layer

File:
```text
models/staging/stg_taxi_trips.sql
```

Responsibilities:
- Schema normalization
- Data quality filtering
- Null handling
- Basic validation

Examples:
- Remove invalid fares
- Remove negative tips
- Remove impossible trip distances

---

## 2. Intermediate Layer

File:
```text
models/intermediate/int_trip_features.sql
```

Responsibilities:
- Business feature engineering
- Time-based transformations
- Derived metrics

Generated features:
- trip_duration_min
- pickup_hour
- is_weekend
- avg_speed_mph
- tip_pct
- is_airport_trip
- time_of_day

---

## 3. Mart Layer

File:
```text
models/marts/daily_metrics.sql
```

Responsibilities:
- Aggregated business metrics
- Reporting tables
- Analytics-ready datasets

Metrics:
- total_trips
- avg_fare
- avg_tip
- avg_distance
- avg_duration
- avg_tip_pct

---

# Data Quality

dbt tests are implemented using:

- not_null
- accepted_values

Example validations:
- payment_type must be valid
- fare_amount cannot be null
- trip_distance cannot be null

---

# Running the Project

## 1. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

---

## 2. Install dbt

```bash
pip install dbt-duckdb plotly streamlit
```

---

## 3. Verify dbt Setup

```bash
dbt debug
```

---

## 4. Run dbt Models

```bash
dbt run
```

---

## 5. Run Tests

```bash
dbt test
```

---

## 6. Generate Documentation

```bash
dbt docs generate
dbt docs serve
```

Open:
```text
http://localhost:8080
```

---

# Key Concepts Demonstrated

- ELT Architecture
- Layered Data Modeling
- Analytics Engineering
- Warehouse-Native SQL Transformations
- Modular SQL Pipelines
- Data Quality Testing
- Business Metric Engineering
- dbt Dependency Management
- Local Warehouse Simulation with DuckDB

---

# Original Spark Pipeline

The original implementation included:
- Spark ETL pipeline
- Partitioned Parquet warehouse
- Machine Learning pipeline
- FastAPI serving
- Streamlit dashboard

This dbt project focuses specifically on the analytics engineering and ELT transformation layer.

---

# Future Improvements

Potential extensions:
- BigQuery deployment
- Incremental dbt models
- Airflow orchestration
- CI/CD integration
- dbt snapshots
- Production warehouse deployment
- BI dashboard integration

---

\
