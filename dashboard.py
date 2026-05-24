import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NYC Taxi ELT Analytics",
    page_icon="🚕",
    layout="wide"
)

# =========================================================
# DATABASE CONNECTION
# =========================================================

conn = duckdb.connect("nyc_taxi.duckdb")

# =========================================================
# TITLE
# =========================================================

st.title("🚕 NYC Taxi ELT Analytics Dashboard")
st.markdown("""
Modern Analytics Engineering Dashboard built using:

- dbt
- DuckDB
- SQL
- ELT Architecture
- Streamlit
""")

st.divider()

# =========================================================
# LOAD DATA
# =========================================================

fact_df = conn.execute("""
SELECT *
FROM fact_trips
""").fetchdf()

daily_df = conn.execute("""
SELECT *
FROM daily_metrics
""").fetchdf()

payment_df = conn.execute("""
SELECT *
FROM payment_type_analysis
""").fetchdf()

airport_df = conn.execute("""
SELECT *
FROM airport_trip_analysis
""").fetchdf()

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🔍 Filters")

selected_time = st.sidebar.multiselect(
    "Select Time of Day",
    options=fact_df["time_of_day"].unique(),
    default=fact_df["time_of_day"].unique()
)

filtered_df = fact_df[
    fact_df["time_of_day"].isin(selected_time)
]

# =========================================================
# KPI SECTION
# =========================================================

st.header("📊 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Trips",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Average Fare",
        f"${filtered_df['fare_amount'].mean():.2f}"
    )

with col3:
    st.metric(
        "Average Tip %",
        f"{filtered_df['tip_pct'].mean()*100:.2f}%"
    )

with col4:
    st.metric(
        "Average Distance",
        f"{filtered_df['trip_distance'].mean():.2f} mi"
    )

st.divider()

# =========================================================
# TIME OF DAY ANALYSIS
# =========================================================

st.header("🕒 Time of Day Analysis")

time_chart = (
    filtered_df
    .groupby("time_of_day")
    .agg({
        "fare_amount": "mean",
        "trip_distance": "mean"
    })
    .reset_index()
)

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        time_chart,
        x="time_of_day",
        y="fare_amount",
        title="Average Fare by Time of Day"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.pie(
        filtered_df,
        names="time_of_day",
        title="Trip Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================================================
# PAYMENT ANALYSIS
# =========================================================

st.header("💳 Payment Type Analysis")

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        payment_df,
        x="payment_type",
        y="avg_tip_pct",
        title="Average Tip % by Payment Type"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.scatter(
        payment_df,
        x="total_trips",
        y="avg_fare",
        size="avg_tip",
        color="payment_type",
        title="Payment Behavior Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================================================
# AIRPORT ANALYSIS
# =========================================================

st.header("✈️ Airport Trip Analysis")

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        airport_df,
        x="is_airport_trip",
        y="avg_fare",
        title="Airport vs Non-Airport Fare"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        airport_df,
        x="is_airport_trip",
        y="avg_duration",
        title="Trip Duration Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================================================
# WEEKEND ANALYSIS
# =========================================================

st.header("📅 Weekend vs Weekday")

weekend_chart = (
    filtered_df
    .groupby("is_weekend")
    .agg({
        "fare_amount": "mean",
        "trip_distance": "mean",
        "tip_pct": "mean"
    })
    .reset_index()
)

fig = px.line(
    weekend_chart,
    x="is_weekend",
    y=["fare_amount", "trip_distance"],
    markers=True,
    title="Weekend Business Metrics"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================================================
# HEATMAP
# =========================================================

st.header("🔥 Trip Density Heatmap")

heat_df = (
    filtered_df
    .groupby(["pickup_hour", "payment_type"])
    .size()
    .reset_index(name="trip_count")
)

fig = px.density_heatmap(
    heat_df,
    x="pickup_hour",
    y="payment_type",
    z="trip_count",
    title="Trips by Hour and Payment Type"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================================================
# RAW DATA
# =========================================================

st.header("📄 Raw Data Preview")

st.dataframe(filtered_df.head(100))

st.divider()

# =========================================================
# SQL QUERY SECTION
# =========================================================

st.header("🧠 SQL Query Playground")

query = st.text_area(
    "Write SQL Query",
    value="""
SELECT
    time_of_day,
    COUNT(*) AS total_trips,
    AVG(fare_amount) AS avg_fare
FROM fact_trips
GROUP BY time_of_day
"""
)

if st.button("Run Query"):

    try:

        result_df = conn.execute(query).fetchdf()

        st.success("Query Executed Successfully!")

        st.dataframe(result_df)

    except Exception as e:

        st.error(f"Error: {e}")

st.divider()

# =========================================================
# ARCHITECTURE SECTION
# =========================================================

st.header("🏗️ ELT Architecture")

st.markdown("""
```text
Raw Parquet Files
        ↓
dbt Staging Models
        ↓
dbt Intermediate Models
        ↓
dbt Mart Tables
        ↓
DuckDB Warehouse
        ↓
Streamlit Dashboard
            """)

# =========================================================
# PROJECT DETAILS
# =========================================================

st.header("📘 Project Details")

st.markdown("""

Technologies Used
dbt
DuckDB
SQL
Streamlit
Plotly
Parquet
Analytics Engineering Concepts
ELT Architecture
Layered Data Modeling
Data Quality Testing
Warehouse-Native SQL
Business Metrics Engineering
Analytics Marts
Lineage & DAG Modeling
Models Built
stg_taxi_trips
int_trip_features
int_trip_quality
fact_trips
daily_metrics
airport_trip_analysis
payment_type_analysis
""")
# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption("Built using dbt + DuckDB + Streamlit 🚀")

st.markdown("""
Run using:

```bash
streamlit run dashboard.py
```
""")