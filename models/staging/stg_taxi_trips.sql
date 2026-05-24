-- cleaning and quality filtering layer for the raw data for the yellow taxi trips = filter_invalid_rows() in spark
-- The staging layer standardizes raw records and applies data quality validations before downstream transformations.

SELECT

    vendorid,
    passenger_count,
    trip_distance,
    ratecodeid,
    payment_type,

    pulocationid,
    dolocationid,

    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    congestion_surcharge,
    airport_fee,
    total_amount,

    tpep_pickup_datetime,
    tpep_dropoff_datetime,

    store_and_fwd_flag

FROM read_parquet('data/raw/yellow_tripdata_2023-01.parquet') -- directly reading from the raw data file in the staging layer - Extraction logic but not.

WHERE fare_amount >= 2.5
  AND fare_amount <= 500

  AND trip_distance > 0
  AND trip_distance <= 100

  AND total_amount > 0

  AND tip_amount >= 0

  AND payment_type IN (1,2,3,4,5,6)

  AND tpep_dropoff_datetime > tpep_pickup_datetime