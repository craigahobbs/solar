[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md)


# Powerwall

~~~ line-chart
title: From Powerwall (Monthly)
width: 1000
height: 350

dataURL: solar.csv

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: From Powerwall (kWh)
aggregation.measures.0.function: Average

xField: MONTH(Date time)
yFields.0: AVERAGE(From Powerwall (kWh))

precision: 1
datetime: Day

xTicks.start.datetime: 2020-04-01
xTicks.end.datetime: 2021-12-01
xTicks.count: 21
xTicks.skip: 3

yTicks.start.number: 0
yTicks.end.number: 30
yTicks.count: 4
~~~

~~~ line-chart
title: From Powerwall
width: 1000
height: 350

dataURL: solar.csv

xField: Date time
yFields.0: From Powerwall (kWh)

precision: 1
datetime: Day

xTicks.start.datetime: 2020-04-01
xTicks.end.datetime: 2021-12-01
xTicks.count: 21
xTicks.skip: 3

yTicks.start.number: 0
yTicks.end.number: 50
yTicks.count: 6
~~~
