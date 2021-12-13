[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
Powerwall |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Powerwall

~~~ line-chart
title: From Powerwall (Monthly)
width: 900
height: 350

data.url: solar.csv

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date time]), month([Date time]), 1)

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categoryFields.0: Month
aggregation.measures.0.field: From Powerwall (kWh)
aggregation.measures.0.function: Average

precision: 1
datetime: Day

xField: Month
yFields.0: AVERAGE(From Powerwall (kWh))

yTicks.start.number: 0
yTicks.end.number: 30
yTicks.count: 4

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value.live.value: Year
~~~

~~~ line-chart
title: From Powerwall
width: 900
height: 350

data.url: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

precision: 1
datetime: Day

xField: Date time
yFields.0: From Powerwall (kWh)

yTicks.start.number: 0
yTicks.end.number: 50
yTicks.count: 6

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value.live.value: Year
~~~
