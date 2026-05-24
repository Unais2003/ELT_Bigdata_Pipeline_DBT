SELECT *

FROM {{ ref('fact_trips') }}

WHERE payment_type NOT IN (1,2,3,4,5,6)