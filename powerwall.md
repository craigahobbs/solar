[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
Powerwall |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Powerwall

~~~ line-chart
title: 'From Powerwall (Monthly)'
width: 900
height: 350

data.url: solar.csv

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date time]), month([Date time]), 1)

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()), month(now()) + 1, 1)

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Month
aggregation.measures.0.field: From Powerwall (kWh)
aggregation.measures.0.function: Average

precision: 1
datetime: Month

xField: Month
yFields.0: AVERAGE(From Powerwall (kWh))

yTicks.start: 0
yTicks.end: 30
yTicks.count: 4

xTicks.start: start
xTicks.end: date(year(end), month(end) - 1, 1)
xTicks.count: ((12 * (year(end) - year(start))) - month(start)) + month(end)
xTicks.skip: 2

xAnnotations.0.value: date(year(end), 1, 1)
~~~

~~~ line-chart
title: 'From Powerwall'
width: 900
height: 350

data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()), month(now()) + 1, 1)

filters.0: ([Date time] >= start) && ([Date time] < end)

precision: 1
datetime: Month

xField: Date time
yFields.0: From Powerwall (kWh)

yTicks.start: 0
yTicks.end: 50
yTicks.count: 6

xTicks.start: start
xTicks.end: date(year(end), month(end) - 1, 1)
xTicks.count: ((12 * (year(end) - year(start))) - month(start)) + month(end)
xTicks.skip: 2

xAnnotations.0.value: date(year(end), 1, 1)
~~~
