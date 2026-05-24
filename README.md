# 🚕 NYC Taxi ELT Analytics Engineering Project

Modern Analytics Engineering pipeline built using:

- dbt
- DuckDB
- SQL
- Streamlit
- Plotly
- Parquet

This project demonstrates a complete ELT (Extract, Load, Transform) workflow for processing NYC Yellow Taxi trip data into analytics-ready business models and interactive dashboards.

---

# 📌 Project Overview

This project simulates a modern cloud-style analytics engineering architecture inspired by platforms like:

- Google BigQuery
- Snowflake
- Databricks SQL

The original implementation was a Spark-based ETL pipeline.  
The transformation layer was later redesigned into a warehouse-native ELT workflow using dbt and DuckDB.

The project demonstrates:

- ELT architecture
- Layered data modeling
- Business metric engineering
- SQL transformations
- dbt testing
- Data lineage
- Interactive analytics dashboards

---

# 🏗️ ELT Architecture

```text
Raw Parquet Files
        ↓
DuckDB Warehouse
        ↓
dbt Staging Models
        ↓
dbt Intermediate Models
        ↓
dbt Mart Models
        ↓
Analytics Dashboard
```

---

# 🔄 What is ELT?

## Traditional ETL

```text
Extract → Transform → Load
```

Data is transformed BEFORE loading into the warehouse.

Example:
- Spark transformations
- Python processing
- Then storing cleaned data

---

## Modern ELT

```text
Extract → Load → Transform
```

Raw data is first loaded into the warehouse, and transformations happen INSIDE the warehouse using SQL.

This is the architecture used by:
- BigQuery
- Snowflake
- Redshift
- dbt-based analytics stacks

---

# 🧠 What is dbt?

## dbt = Data Build Tool

dbt is a framework used for:

- SQL transformations
- Data modeling
- Dependency management
- Automated testing
- Documentation generation
- Lineage tracking

dbt allows analytics engineers to organize SQL transformations into modular pipelines.

---

# 🦆 What is DuckDB?

DuckDB is a lightweight analytical database optimized for:

- OLAP workloads
- SQL analytics
- Parquet processing
- Local analytics engineering workflows

DuckDB can directly query:
- Parquet
- CSV
- JSON

without requiring a traditional database server.

---

# 🎯 Why DuckDB Was Used

DuckDB was used because:

- lightweight local warehouse
- no cloud setup required
- dbt-compatible
- extremely fast analytics engine
- direct parquet querying
- perfect for ELT prototyping

It simulates warehouse-native transformations locally.

---

# 📂 Project Structure

```text
ELT_nyc_taxi_dbt/
│
├── analyses/
│   ├── monthly_revenue_analysis.sql
│   └── peak_hour_analysis.sql
│
├── data/
│   └── raw/
│       ├── yellow_tripdata_2023-01.parquet
│       ├── yellow_tripdata_2023-02.parquet
│       ├── yellow_tripdata_2023-03.parquet
│       └── taxi_zone_lookup.csv
│
├── docs/
│
├── logs/
│
├── macros/
│   ├── calculate_tip_pct.sql
│   └── categorize_time_of_day.sql
│
├── models/
│   ├── staging/
│   │   ├── stg_taxi_trips.sql
│   │   ├── stg_taxi_zones.sql
│   │   └── schema.yml
│   │
│   ├── intermediate/
│   │   ├── int_trip_features.sql
│   │   ├── int_trip_quality.sql
│   │   └── schema.yml
│   │
│   ├── marts/
│   │   ├── fact_trips.sql
│   │   ├── daily_metrics.sql
│   │   ├── airport_trip_analysis.sql
│   │   ├── payment_type_analysis.sql
│   │   └── schema.yml
│   │
│   └── sources.yml
│
├── seeds/
│
├── snapshots/
│
├── target/
│
├── tests/
│   ├── assert_positive_fare.sql
│   ├── assert_valid_payment_type.sql
│   └── assert_valid_trip_duration.sql
│
├── dashboard.py
├── dbt_project.yml
├── profiles.yml
├── README.md
└── .gitignore
```

---

# 📊 Layered Data Modeling

The project follows layered warehouse modeling architecture.

---

# 1️⃣ Staging Layer

Folder:

```text
models/staging/
```

Purpose:
- clean raw data
- normalize schema
- apply quality filters
- validate records

Models:
- stg_taxi_trips
- stg_taxi_zones

Responsibilities:
- remove invalid fares
- remove impossible trip distances
- validate payment types
- filter invalid timestamps

Equivalent to:
- Spark cleaning layer

---

# 2️⃣ Intermediate Layer

Folder:

```text
models/intermediate/
```

Purpose:
- feature engineering
- business logic
- derived metrics

Models:
- int_trip_features
- int_trip_quality

Generated Features:
- trip_duration_min
- pickup_hour
- avg_speed_mph
- tip_pct
- is_airport_trip
- is_weekend
- time_of_day

Equivalent to:
- Spark feature engineering

---

# 3️⃣ Mart Layer

Folder:

```text
models/marts/
```

Purpose:
- analytics-ready business datasets
- KPI tables
- reporting models

Models:
- fact_trips
- daily_metrics
- airport_trip_analysis
- payment_type_analysis

Responsibilities:
- aggregated business metrics
- dashboard-ready tables
- analytical reporting

---

# 🧪 Data Quality Testing

Implemented dbt tests:

- not_null
- accepted_values
- custom SQL assertions

Examples:
- payment_type must be valid
- fare_amount cannot be null
- trip_duration must be positive

---

# 🔗 dbt Lineage & Dependency Graph

dbt models reference each other using:

```sql
{{ ref('model_name') }}
```

Example:

```sql
FROM {{ ref('stg_taxi_trips') }}
```

This creates:
- dependency graphs
- lineage DAGs
- execution ordering

---

# 🧱 Materializations

| Layer | Materialization |
|---|---|
| staging | view |
| intermediate | view |
| marts | table |

---

# Why?

## Views
Used for lightweight transformations.

## Tables
Used for analytics marts for faster reporting performance.

---

# 📈 Dashboard Features

The Streamlit dashboard includes:

- Business KPIs
- Payment analysis
- Airport trip analytics
- Time-of-day trends
- Heatmaps
- Interactive filters
- SQL query playground
- Data export
- Business insights

---

# 🖥️ Dashboard Architecture

```text
dbt Models
      ↓
DuckDB Warehouse
      ↓
Streamlit Dashboard
```

---

# 📊 Output Models Created

The dbt pipeline creates:

| Model | Type |
|---|---|
| stg_taxi_trips | View |
| stg_taxi_zones | View |
| int_trip_features | View |
| int_trip_quality | View |
| fact_trips | Table |
| daily_metrics | Table |
| airport_trip_analysis | Table |
| payment_type_analysis | Table |

---

# 📦 Technologies Used

| Component | Technology |
|---|---|
| Transformation Framework | dbt |
| Warehouse Engine | DuckDB |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Data Format | Parquet |
| Query Language | SQL |
| Original Pipeline | PySpark |

---

# ⚙️ Setup Instructions

---

# 1️⃣ Create Virtual Environment

```bash
python3.11 -m venv venv
```

---

# 2️⃣ Activate Environment

macOS/Linux:

```bash
source venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
<<<<<<< HEAD
pip install dbt-duckdb plotly streamlit
=======
pip install dbt-duckdb streamlit duckdb pandas plotly
>>>>>>> 59a89c6 (feat : added streamlit dashboard)
```

---

# 4️⃣ Verify dbt Setup

```bash
dbt debug
```

---

# 5️⃣ Run dbt Models

```bash
dbt run
```

---

# 6️⃣ Run Data Tests

```bash
dbt test
```

---

# 7️⃣ Generate dbt Documentation

```bash
dbt docs generate
```

---

# 8️⃣ Serve dbt Documentation

```bash
dbt docs serve
```

Open:
```text
http://localhost:8080
```

---

# 9️⃣ Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

---

# 🔍 SQL Query Playground

The dashboard includes a built-in SQL editor where users can:

- write custom SQL queries
- query warehouse tables
- explore business metrics
- visualize results interactively

---

# 📌 Key Analytics Engineering Concepts Demonstrated

This project demonstrates:

- ELT Architecture
- Analytics Engineering
- Warehouse-Native SQL
- Layered Data Modeling
- dbt Transformations
- Data Quality Testing
- Business Metric Engineering
- Lineage DAG Modeling
- SQL Dependency Management
- Interactive BI Dashboards

---

# 🚀 Future Improvements

Potential production extensions:

- BigQuery deployment
- Incremental dbt models
- Airflow orchestration
- CI/CD pipelines
- dbt snapshots
- Production warehouse deployment
- Real-time ingestion
- BI tool integration

---

<<<<<<< HEAD
\
=======
# 💬 Interview Talking Points

This project demonstrates:

- ETL → ELT migration thinking
- Modern analytics engineering workflows
- Warehouse-native transformations
- SQL-based business modeling
- Layered architecture design
- Data quality engineering
- Dashboard integration
- dbt lineage & dependency management

---

# 📌 Final Summary

This project successfully adapts a Spark-based ETL pipeline into a modern analytics engineering ELT workflow using dbt and DuckDB.

The pipeline transforms raw NYC taxi parquet data into analytics-ready business models using modular SQL transformations, automated testing, lineage-driven dependency management, and interactive dashboarding.

The project simulates real-world warehouse analytics workflows commonly used in modern cloud data platforms.
>>>>>>> 59a89c6 (feat : added streamlit dashboard)
