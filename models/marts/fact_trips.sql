-- taxi trip as analytical event, central analytics fact table : fact tables contain measurable business events.
SELECT

    vendorid,
    passenger_count,
    payment_type,

    pulocationid,
    dolocationid,

    fare_amount,
    tip_amount,
    total_amount,

    trip_distance,
    trip_duration_min,

    pickup_hour,

    avg_speed_mph,
    tip_pct,

    is_airport_trip,
    is_weekend,
    time_of_day,

    tpep_pickup_datetime,
    tpep_dropoff_datetime

FROM {{ ref('int_trip_quality') }}