-- urealestic duration and speed values can be due to data quality issues, outliers, or errors in the data collection process. By filtering out these records, we can improve the overall quality of our dataset and ensure that our analysis is based on more reliable data.

SELECT *

FROM {{ ref('int_trip_features') }}

WHERE trip_duration_min > 0
  AND trip_duration_min <= 300

  AND avg_speed_mph > 0
  AND avg_speed_mph <= 80

  AND tip_pct >= 0
  AND tip_pct <= 1