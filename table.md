[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
Table


# Monthly Table

~~~ data-table
data.url: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: Year
aggregation.categories.1.field: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Home (kWh)
aggregation.measures.2.function: Sum

sorts.0.field: Year
sorts.0.desc: true
sorts.1.field: Month
sorts.1.desc: true

precision: 1
datetime: Month

categoryFields.0: Year
~~~
