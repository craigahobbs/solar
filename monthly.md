[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
Monthly |
[Table](#url=table.md)


# Monthly

~~~ line-chart
title: 'Monthly Solar Energy'
width: 900
height: 350

data.url: data/solar.csv

calc.0.name: Year
calc.0.expr: year([Date time])
calc.1.name: Month
calc.1.expr: month([Date time])

filter: [Date time] >= date(2020, 6, 1)

agg.category.0: Year
agg.category.1: Month
agg.measure.0.field: Solar Energy (kWh)
agg.measure.0.func: Sum

x: Month
y.0: Solar Energy (kWh)
color: Year

xtick.count: 12

ytick.start: 0
ytick.end: 2500
ytick.count: 11
ytick.skip: 1

precision: 1
datetime: Day
~~~

~~~ line-chart
title: 'Monthly Power Usage'
width: 900
height: 350

data.url: data/solar.csv

calc.0.name: Year
calc.0.expr: year([Date time])
calc.1.name: Month
calc.1.expr: month([Date time])

filter: [Date time] >= date(2020, 6, 1)

agg.category.0: Year
agg.category.1: Month
agg.measure.0.field: Home (kWh)
agg.measure.0.func: Sum

x: Month
y.0: Home (kWh)
color: Year

xtick.count: 12

ytick.start: 0
ytick.end: 1500
ytick.count: 7

precision: 1
datetime: Day
~~~

~~~ line-chart
title: 'Monthly Solar Offset'
width: 900
height: 350

data.url: data/solar.csv

calc.0.name: Year
calc.0.expr: year([Date time])
calc.1.name: Month
calc.1.expr: month([Date time])
calc.2.name: Solar Offset (kWh)
calc.2.expr: [Solar Energy (kWh)] - [Home (kWh)]

filter: [Date time] >= date(2020, 6, 1)

agg.category.0: Year
agg.category.1: Month
agg.measure.0.field: Solar Offset (kWh)
agg.measure.0.func: Sum

x: Month
y.0: Solar Offset (kWh)
color: Year

xtick.count: 12

ytick.start: -1000
ytick.end: 1500
ytick.count: 11
ytick.skip: 1

yline.0.value: 0
yline.0.label: ''

precision: 1
datetime: Day
~~~
