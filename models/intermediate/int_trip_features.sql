-- business logic layer - feature engineering layer
SELECT

    *,

    DATEDIFF(
        'minute',
        tpep_pickup_datetime,
        tpep_dropoff_datetime
    ) AS trip_duration_min,

    EXTRACT(HOUR FROM tpep_pickup_datetime) AS pickup_hour,

    EXTRACT(DAYOFWEEK FROM tpep_pickup_datetime) AS pickup_dayofweek,

    CASE
        WHEN EXTRACT(DAYOFWEEK FROM tpep_pickup_datetime) IN (1,7)
        THEN 1
        ELSE 0
    END AS is_weekend,

    CASE
        WHEN EXTRACT(HOUR FROM tpep_pickup_datetime) BETWEEN 0 AND 5
            THEN 'night'

        WHEN EXTRACT(HOUR FROM tpep_pickup_datetime) BETWEEN 6 AND 11
            THEN 'morning'

        WHEN EXTRACT(HOUR FROM tpep_pickup_datetime) BETWEEN 12 AND 17
            THEN 'afternoon'

        ELSE 'evening'
    END AS time_of_day,

    ROUND(
        trip_distance /
        (
            DATEDIFF(
                'second',
                tpep_pickup_datetime,
                tpep_dropoff_datetime
            ) / 3600.0
        ),
        2
    ) AS avg_speed_mph,

    ROUND(
        tip_amount / fare_amount,
        4
    ) AS tip_pct,

    CASE
        WHEN pulocationid IN (1,132,138)
          OR dolocationid IN (1,132,138)
        THEN 1
        ELSE 0
    END AS is_airport_trip

FROM {{ ref('stg_taxi_trips') }} 
-- here the dbt uses dependency management to reference the previous dbt model as source for transformations - This creates:

-- lineage
-- DAG
-- dependency graph"