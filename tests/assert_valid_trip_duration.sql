SELECT *

FROM {{ ref('fact_trips') }}

WHERE trip_duration_min <= 0