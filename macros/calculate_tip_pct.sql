-- Reusable SQL logic. Equivalent to spark : reusable transformation functions.

{% macro calculate_tip_pct(tip_amount, fare_amount) %}

ROUND(
    {{ tip_amount }} / NULLIF({{ fare_amount }}, 0),
    4
)

{% endmacro %}

