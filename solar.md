[Home](#url=README.md) |
Solar |
[Self-Powered](#url=self-powered.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Solar Energy Generated and Power Used

~~~ line-chart
width: 1100
height: 350

data.url: data/solar.csv

var.vStart: date(year(now()) - 1, 1, 1)
var.vEnd: date(year(now()), month(now()) + 1, 1)

calc.0.name: Month
calc.0.expr: date(year([Date time]), month([Date time]), 1)

filter: [Date time] >= vStart && [Date time] < vEnd

agg.category.0: Month
agg.measure.0.field: Home (kWh)
agg.measure.0.func: Sum
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Sum

x: Month
y.0: Home (kWh)
y.1: Solar Energy (kWh)

xtick.start: vStart
xtick.end: date(year(vEnd), month(vEnd) - 1, 1)
xtick.count: ((12 * (year(vEnd) - year(vStart))) - month(vStart)) + month(vEnd)
xtick.skip: 2

ytick.start: 0
ytick.end: 2500
ytick.count: 11
ytick.skip: 1

xline.0.value: date(year(vEnd), 1, 1)

precision: 1
datetime: Month
~~~


### Annual Solar Offset

~~~ data-table
data.url: data/solar.csv

var.vStart: date(year(now()) - 1, 1, 1)
var.vEnd: date(year(now()), month(now()) + 1, 1)

calc.0.name: Year
calc.0.expr: year([Date time])
calc.1.name: Solar Offset (kWh)
calc.1.expr: [Solar Energy (kWh)] - [Home (kWh)]

filter: [Date time] >= vStart && [Date time] < vEnd

agg.category.0: Year
agg.measure.0.field: Solar Offset (kWh)
agg.measure.0.func: Sum
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Sum
agg.measure.2.field: Home (kWh)
agg.measure.2.func: Sum

sort.0.field: Year
sort.0.desc: true

precision: 1
datetime: Year
~~~


### Average Daily Solar Offset by Month

~~~ data-table
data.url: data/solar.csv

calc.0.name: Year
calc.0.expr: year([Date time])
calc.1.name: Month
calc.1.expr: month([Date time])
calc.2.name: Offset (kWh)
calc.2.expr: [Solar Energy (kWh)] - [Home (kWh)]

filter: [Date time] >= date(2020, 6, 1)

agg.category.0: Year
agg.category.1: Month
agg.measure.0.field: Offset (kWh)
agg.measure.0.func: Average
agg.measure.1.name: Solar (kWh)
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Average
agg.measure.2.field: Home (kWh)
agg.measure.2.func: Average

sort.0.field: Year
sort.0.desc: true
sort.1.field: Month
sort.1.desc: true

category.0: Year

precision: 1
~~~
