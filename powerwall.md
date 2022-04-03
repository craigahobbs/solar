[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Self-Powered](#url=self-powered.md) |
[Grid](#url=grid.md) |
Powerwall |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Powerwall

~~~ line-chart
title: 'From Powerwall (Monthly)'
width: 900
height: 350

data.url: data/solar.csv

calc.0.name: Month
calc.0.expr: date(year([Date time]), month([Date time]), 1)

var.start: date(year(now()) - 1, 1, 1)
var.end: date(year(now()), month(now()) + 1, 1)

filter: [Date time] >= start && [Date time] < end

agg.category.0: Month
agg.measure.0.name: Average From Powerwall (kWh)
agg.measure.0.field: From Powerwall (kWh)
agg.measure.0.func: Average

x: Month
y.0: Average From Powerwall (kWh)

xtick.start: start
xtick.end: date(year(end), month(end) - 1, 1)
xtick.count: ((12 * (year(end) - year(start))) - month(start)) + month(end)
xtick.skip: 2

ytick.start: 0
ytick.end: 30
ytick.count: 4

xline.0.value: date(year(end), 1, 1)

precision: 1
datetime: Month
~~~

~~~ line-chart
title: 'From Powerwall'
width: 900
height: 350

data.url: data/solar.csv

var.start: date(year(now()) - 1, 1, 1)
var.end: date(year(now()), month(now()) + 1, 1)

filter: [Date time] >= start && [Date time] < end

x: Date time
y.0: From Powerwall (kWh)

xtick.start: start
xtick.end: date(year(end), month(end) - 1, 1)
xtick.count: ((12 * (year(end) - year(start))) - month(start)) + month(end)
xtick.skip: 2

ytick.start: 0
ytick.end: 50
ytick.count: 6

xline.0.value: date(year(end), 1, 1)

precision: 1
datetime: Month
~~~
