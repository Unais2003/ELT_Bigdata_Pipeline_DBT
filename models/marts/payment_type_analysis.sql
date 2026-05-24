-- mart for payment type analysis
SELECT

    payment_type,

    COUNT(*) AS total_trips,

    ROUND(AVG(fare_amount), 2) AS avg_fare,

    ROUND(AVG(tip_amount), 2) AS avg_tip,

    ROUND(AVG(tip_pct), 4) AS avg_tip_pct

FROM {{ ref('fact_trips') }}

GROUP BY payment_type