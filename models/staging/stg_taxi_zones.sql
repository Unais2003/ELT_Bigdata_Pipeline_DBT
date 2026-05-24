-- Loads taxi zone lookup reference data.
SELECT *

FROM read_csv_auto(
    'data/raw/taxi_zone_lookup.csv'
)