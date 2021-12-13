[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
Table


# Monthly Table

~~~ data-table
data.url: solar.csv

calculatedFields.0.name: Year
calculatedFields.0.expression: year([Date time])
calculatedFields.1.name: Month
calculatedFields.1.expression: month([Date time])
calculatedFields.2.name: Solar Offset (kWh)
calculatedFields.2.expression: [Solar Energy (kWh)] - [Home (kWh)]

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categoryFields.0: Year
aggregation.categoryFields.1: Month
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
