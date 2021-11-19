[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md)


# Powerwall

~~~ line-chart
title: From Powerwall (Monthly)
width: 900
height: 350

dataURL: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: From Powerwall (kWh)
aggregation.measures.0.function: Average

xField: MONTH(Date time)
yFields.0: AVERAGE(From Powerwall (kWh))

precision: 1
datetime: Day

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

dataURL: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

xField: Date time
yFields.0: From Powerwall (kWh)

precision: 1
datetime: Day

yTicks.start.number: 0
yTicks.end.number: 50
yTicks.count: 6

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value.live.value: Year
~~~
