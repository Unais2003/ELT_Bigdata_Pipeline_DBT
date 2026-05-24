# Complete ELT dbt + DuckDB Documentation

You can directly put this into your `README.md` or a separate `docs/architecture.md`.

---

# NYC Taxi ELT Pipeline using dbt + DuckDB

# 1. Project Overview

This project demonstrates a modern **ELT (Extract, Load, Transform)** analytics engineering workflow using:

* dbt
* DuckDB
* SQL
* Parquet files

The project processes NYC Yellow Taxi trip data and transforms raw trip records into analytics-ready business models using layered dbt transformations.

Originally, the project was implemented as a Spark-based ETL pipeline. The transformation logic was later adapted into a modern warehouse-native ELT architecture inspired by cloud data warehouse systems like Google BigQuery.

---

# 2. What is ELT?

## Traditional ETL

```text
Extract → Transform → Load
```

Data is transformed BEFORE loading into the warehouse.

Example:

* Spark transformations
* Python processing
* Then loading cleaned data

This is what the original Spark pipeline did.

---

## Modern ELT

```text
Extract → Load → Transform
```

Raw data is first loaded into the warehouse, and transformations happen INSIDE the warehouse using SQL.

This is the modern analytics engineering approach used with:

* BigQuery
* Snowflake
* Redshift
* Databricks SQL
* dbt

---

# 3. What is dbt?

## dbt = Data Build Tool

dbt is a framework used for:

* SQL transformations
* Data modeling
* Data quality testing
* Documentation
* Dependency management

dbt allows analytics engineers to organize SQL transformations into modular pipelines.

---

# What dbt Does

dbt handles:

* SQL transformations
* Model dependencies
* Testing
* Documentation
* Lineage graphs

dbt does NOT usually handle:

* ingestion
* streaming
* orchestration

---

# 4. What is DuckDB?

## DuckDB

DuckDB is a lightweight analytical database engine optimized for:

* OLAP workloads
* analytical SQL queries
* Parquet processing

DuckDB can directly query:

* Parquet
* CSV
* JSON

without loading data into traditional databases.

---

# Why DuckDB Was Used

DuckDB was used because:

* lightweight local warehouse
* no cloud setup required
* supports dbt
* excellent for analytics engineering demos
* can query parquet files directly

DuckDB simulates warehouse-style ELT workflows locally.

---

# 5. Project Architecture

```text
Raw Parquet Files
        ↓
Staging Models
        ↓
Intermediate Models
        ↓
Mart Models
        ↓
Analytics / Reporting
```

---

# 6. Where ELT Happens

## E = Extract

Raw taxi parquet files are downloaded.

Location:

```text
data/raw/
```

Files:

* yellow_tripdata_2023-01.parquet
* yellow_tripdata_2023-02.parquet
* yellow_tripdata_2023-03.parquet

---

## L = Load

The raw parquet files are directly queried by DuckDB.

Example:

```sql
FROM read_parquet('data/raw/yellow_tripdata_2023-01.parquet')
```

This simulates loading raw data into a warehouse.

In real production architecture:

* raw data would be loaded into BigQuery tables.

---

## T = Transform

Transformations happen inside dbt SQL models.

Example:

* filtering invalid rows
* feature engineering
* aggregations
* metrics creation

This is the main ELT transformation layer.

---

# 7. Layered Data Modeling

The project follows layered modeling architecture.

---

# Staging Layer

Folder:

```text
models/staging/
```

Purpose:

* clean raw data
* normalize schema
* apply quality checks

File:

```text
stg_taxi_trips.sql
```

Responsibilities:

* remove invalid fares
* remove invalid trip distances
* validate payment types
* filter invalid timestamps

Equivalent to:

* Spark `filter_invalid_rows()`

---

# Intermediate Layer

Folder:

```text
models/intermediate/
```

Purpose:

* business logic
* feature engineering
* derived metrics

File:

```text
int_trip_features.sql
```

Generated features:

* trip_duration_min
* pickup_hour
* is_weekend
* avg_speed_mph
* tip_pct
* is_airport_trip
* time_of_day

Equivalent to:

* Spark `engineer_features()`

---

# Mart Layer

Folder:

```text
models/marts/
```

Purpose:

* analytics-ready business tables
* KPI reporting
* dashboard-ready datasets

File:

```text
daily_metrics.sql
```

Metrics:

* total_trips
* avg_fare
* avg_tip
* avg_distance
* avg_duration
* avg_tip_pct

Equivalent to:

* PostgreSQL summary aggregation in Spark pipeline

---

# 8. Project Folder Structure

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

# 9. Important Files Explained

# `dbt_project.yml`

Main dbt configuration file.

Defines:

* project name
* model locations
* materialization strategy

---

# `profiles.yml`

Warehouse connection configuration.

In this project:

* connects dbt to DuckDB.

---

# `sources.yml`

Defines raw source tables.

In production:

* these would point to BigQuery raw tables.

---

# `stg_taxi_trips.sql`

Staging model.

Handles:

* cleaning
* validation
* normalization

---

# `int_trip_features.sql`

Intermediate feature model.

Handles:

* derived metrics
* business logic
* feature engineering

---

# `daily_metrics.sql`

Mart model.

Handles:

* aggregations
* KPIs
* reporting tables

---

# `schema.yml`

Defines dbt data quality tests.

Examples:

* not_null
* accepted_values

---

# 10. dbt Materializations

dbt models can become:

* views
* tables
* incremental tables

This project uses:

| Layer        | Materialization |
| ------------ | --------------- |
| staging      | view            |
| intermediate | view            |
| marts        | table           |

---

# Why?

## Views

Used for lightweight transformations without storing duplicate data.

## Tables

Used for aggregated marts to improve analytics performance.

---

# 11. dbt Dependency Management

dbt models reference each other using:

```sql
{{ ref('stg_taxi_trips') }}
```

This creates:

* lineage DAG
* dependency graph
* execution ordering

---

# 12. Data Quality Testing

dbt tests validate data automatically.

Implemented tests:

* not_null
* accepted_values

Examples:

* payment_type must be valid
* fare_amount cannot be null
* trip_distance cannot be null

---

# 13. Documentation & Lineage

dbt automatically generates:

* documentation
* model lineage graphs
* dependency DAGs

Generated using:

```bash
dbt docs generate
dbt docs serve
```

Access:

```text
http://localhost:8080
```

---

# 14. Commands Used

# Create Virtual Environment

```bash
python3.11 -m venv venv
```

---

# Activate Environment

macOS/Linux:

```bash
source venv/bin/activate
```

---

# Install dbt

```bash
pip install dbt-duckdb
```

---

# Verify dbt Setup

```bash
dbt debug
```

---

# Run Models

```bash
dbt run
```

---

# Run Tests

```bash
dbt test
```

---

# Generate Documentation

```bash
dbt docs generate
```

---

# Serve Documentation

```bash
dbt docs serve
```

---

# Open Documentation

```text
http://localhost:8080
```

---

# 15. Output Tables Created

The dbt run created:

| Model             | Type  |
| ----------------- | ----- |
| stg_taxi_trips    | View  |
| int_trip_features | View  |
| daily_metrics     | Table |

Stored inside:

```text
nyc_taxi.duckdb
```

---

# 16. Key Concepts Demonstrated

This project demonstrates:

* ELT Architecture
* Analytics Engineering
* Warehouse-Native SQL
* Layered Data Modeling
* Data Quality Testing
* SQL Transformations
* dbt Lineage DAG
* Modular Pipelines
* Business Metric Engineering
* Local Warehouse Simulation

---

# 17. Future Improvements

Potential production extensions:

* BigQuery deployment
* Incremental dbt models
* Airflow orchestration
* CI/CD integration
* dbt snapshots
* Production cloud warehouse
* BI dashboard integration

---

# 18. Interview Talking Points

This project demonstrates:

* ETL → ELT migration thinking
* warehouse-native analytics engineering
* layered transformation architecture
* SQL transformation modeling
* data quality engineering
* dependency management
* analytics marts
* modern data workflows

---

# 19. Final Summary

This project successfully adapts a Spark-based ETL pipeline into a modern ELT analytics engineering workflow using dbt and DuckDB.

The project demonstrates how raw parquet data can be transformed into analytics-ready business models using modular SQL transformations, layered modeling architecture, automated testing, and lineage-driven dependency management.


| Layer            | Purpose                   | What It Does                                      |
| ---------------- | ------------------------- | ------------------------------------------------- |
| **staging**      | Raw data cleaning layer   | Cleans, validates, renames, standardizes raw data |
| **intermediate** | Business logic layer      | Creates derived features and transformations      |
| **marts**        | Analytics/reporting layer | Builds KPI tables and analytics-ready datasets    |
| **tests**        | Data quality validation   | Ensures data correctness and consistency          |
| **macros**       | Reusable SQL logic        | Stores reusable SQL functions/business logic      |
| **analyses**     | Ad hoc analytics queries  | Used for exploration and business analysis        |
| **docs**         | Documentation layer       | Generates model documentation and metadata        |
| **lineage**      | Dependency graph          | Shows how models depend on each other             |
