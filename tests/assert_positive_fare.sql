-- custom dbt positive fare test
SELECT *

FROM {{ ref('fact_trips') }}

WHERE fare_amount <= 0