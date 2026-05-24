-- Ad hoc business analysis query. dbt analyses/ folder is used for: exploration, business reporting,analytical SQL

SELECT

    DATE_TRUNC('month', tpep_pickup_datetime) AS trip_month,

    SUM(total_amount) AS total_revenue,

    COUNT(*) AS total_trips

FROM {{ ref('fact_trips') }}

GROUP BY 1

ORDER BY 1