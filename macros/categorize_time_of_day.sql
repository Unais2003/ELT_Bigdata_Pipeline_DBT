--  Reusable business logic macro. Categorizes time of day based on hour of pickup. This can be used across multiple models for consistent categorization.

{% macro categorize_time_of_day(hour_column) %}

CASE

    WHEN {{ hour_column }} BETWEEN 0 AND 5
        THEN 'night'

    WHEN {{ hour_column }} BETWEEN 6 AND 11
        THEN 'morning'

    WHEN {{ hour_column }} BETWEEN 12 AND 17
        THEN 'afternoon'

    ELSE 'evening'

END

{% endmacro %}