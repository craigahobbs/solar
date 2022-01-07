[Home](#url=README.md) |
Solar |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Solar

~~~ data-table
data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: year([Date time])
calculatedFields.1.name: Solar Offset (kWh)
calculatedFields.1.expression: [Solar Energy (kWh)] - [Home (kWh)]

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Year
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Home (kWh)
aggregation.measures.2.function: Sum

sorts.0.field: Year
sorts.0.desc: true

precision: 1
datetime: Year
~~~

~~~ line-chart
title: Solar and Home (Monthly)
width: 1100
height: 350

data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date time]), month([Date time]), 1)

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Month
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(Home (kWh))
yFields.1: SUM(Solar Energy (kWh))

yTicks.start: 0
yTicks.end: 2500
yTicks.count: 11
yTicks.skip: 1

xTicks.start: start
xTicks.end: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value: date(year(now()), 1, 1)
~~~

~~~ line-chart
title: Solar Offset (Monthly)
width: 900
height: 350

data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date time]), month([Date time]), 1)
calculatedFields.1.name: Solar Offset (kWh)
calculatedFields.1.expression: [Solar Energy (kWh)] - [Home (kWh)]

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(Solar Offset (kWh))

yTicks.start: -1200
yTicks.end: 1200
yTicks.count: 9
yTicks.skip: 1

xTicks.start: start
xTicks.end: end
xTicks.count: 25
xTicks.skip: 3

yAnnotations.0.value: 0
yAnnotations.0.label: ''

xAnnotations.0.value: date(year(now()), 1, 1)
~~~
