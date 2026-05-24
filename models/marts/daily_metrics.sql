-- analytics mart and reporting table Equivalent to  PostgreSQL aggregation logic

SELECT

    DATE(tpep_pickup_datetime) AS trip_date,

    payment_type,

    time_of_day,

    COUNT(*) AS total_trips,

    ROUND(AVG(fare_amount), 2) AS avg_fare,

    ROUND(AVG(tip_amount), 2) AS avg_tip,

    ROUND(AVG(trip_distance), 2) AS avg_distance,

    ROUND(AVG(trip_duration_min), 2) AS avg_duration,

    ROUND(AVG(tip_pct), 4) AS avg_tip_pct

FROM {{ ref('int_trip_features') }}

GROUP BY 1,2,3