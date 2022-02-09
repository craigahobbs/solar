[Home](#url=README.md) |
[Solar](#url=solar.md) |
Grid |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Grid

~~~ data-table
data.url: solar.csv

var.vStart: date(year(now()) - 1, 1, 1)
var.vEnd: date(year(now()), month(now()) + 1, 1)

calc.0.name: Year
calc.0.expr: date(year([Date time]), 1, 1)
calc.1.name: Grid Surplus (kWh)
calc.1.expr: -[To Grid (kWh)] - [From Grid (kWh)]

filter: [Date time] >= vStart && [Date time] < vEnd

agg.category.0: Year
agg.measure.0.field: Grid Surplus (kWh)
agg.measure.0.func: Sum
agg.measure.1.field: To Grid (kWh)
agg.measure.1.func: Sum
agg.measure.2.field: From Grid (kWh)
agg.measure.2.func: Sum

sort.0.field: Year
sort.0.desc: true

precision: 1
datetime: Year
~~~

~~~ line-chart
title: 'Grid Surplus (Monthly)'
width: 900
height: 350

data.url: solar.csv

var.vStart: date(year(now()) - 1, 1, 1)
var.vEnd: date(year(now()), month(now()) + 1, 1)

calc.0.name: Month
calc.0.expr: date(year([Date time]), month([Date time]), 1)
calc.1.name: Grid Surplus (kWh)
calc.1.expr: -[To Grid (kWh)] - [From Grid (kWh)]

filter: [Date time] >= vStart && [Date time] < vEnd

agg.category.0: Month
agg.measure.0.field: Grid Surplus (kWh)
agg.measure.0.func: Sum

x: Month
y.0: Grid Surplus (kWh)

xtick.start: vStart
xtick.end: date(year(vEnd), month(vEnd) - 1, 1)
xtick.count: ((12 * (year(vEnd) - year(vStart))) - month(vStart)) + month(vEnd)
xtick.skip: 2

ytick.start: -1200
ytick.end: 1200
ytick.count: 9
ytick.skip: 1

xline.0.value: date(year(vEnd), 1, 1)

yline.0.value: 0
yline.0.label: ''

precision: 1
datetime: Month
~~~

~~~ line-chart
title: 'To/From Grid'
width: 1050
height: 350

data.url: solar.csv

var.vStart: date(year(now()) - 1, 1, 1)
var.vEnd: date(year(now()), month(now()) + 1, 1)

filter: [Date time] >= vStart && [Date time] < vEnd

x: Date time
y.0: From Grid (kWh)
y.1: To Grid (kWh)

xtick.start: vStart
xtick.end: date(year(vEnd), month(vEnd) - 1, 1)
xtick.count: ((12 * (year(vEnd) - year(vStart))) - month(vStart)) + month(vEnd)
xtick.skip: 2

ytick.start: -80
ytick.end: 120
ytick.count: 6

xline.0.value: date(year(vEnd), 1, 1)

precision: 1
datetime: Month
~~~

~~~ line-chart
title: 'To/From Grid (Monthly)'
width: 1100
height: 350

data.url: solar.csv

var.vStart: date(year(now()) - 1, 1, 1)
var.vEnd: date(year(now()), month(now()) + 1, 1)

calc.0.name: Month
calc.0.expr: date(year([Date time]), month([Date time]), 1)

filter: [Date time] >= vStart && [Date time] < vEnd

agg.category.0: Month
agg.measure.0.field: From Grid (kWh)
agg.measure.0.func: Sum
agg.measure.1.field: To Grid (kWh)
agg.measure.1.func: Sum

x: Month
y.0: From Grid (kWh)
y.1: To Grid (kWh)

xtick.start: vStart
xtick.end: date(year(vEnd), month(vEnd) - 1, 1)
xtick.count: ((12 * (year(vEnd) - year(vStart))) - month(vStart)) + month(vEnd)
xtick.skip: 2

ytick.start: -1200
ytick.end: 1200
ytick.count: 9

xline.0.value: date(year(vEnd), 1, 1)

precision: 1
datetime: Month
~~~
