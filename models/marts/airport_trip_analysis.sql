-- mart for airport vs non-airport trip analysis.
SELECT

    is_airport_trip,

    COUNT(*) AS total_trips,

    ROUND(AVG(fare_amount), 2) AS avg_fare,

    ROUND(AVG(tip_amount), 2) AS avg_tip,

    ROUND(AVG(trip_distance), 2) AS avg_distance,

    ROUND(AVG(trip_duration_min), 2) AS avg_duration

FROM {{ ref('fact_trips') }}

GROUP BY is_airport_trip