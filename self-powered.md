[Home](#url=README.md) |
[Solar](#url=solar.md) |
Self-Powered |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Self-Powered by Month

~~~ line-chart
width: 900
height: 350

data.url: data/solar.csv

calc.0.name: Date
calc.0.expr: date(year([Date time]), month([Date time]), 1)

filter: [Date time] >= date(2021, 1, 1)

agg.category.0: Date
agg.measure.0.field: Home (kWh)
agg.measure.0.func: Average
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Average
agg.measure.2.field: From Powerwall (kWh)
agg.measure.2.func: Average
agg.measure.3.field: From Grid (kWh)
agg.measure.3.func: Average

aggcalc.0.name: From Solar (kWh)
aggcalc.0.expr: [Home (kWh)] - [From Powerwall (kWh)] - [From Grid (kWh)]
aggcalc.1.name: Self-Powered
aggcalc.1.expr: 100 * ([From Solar (kWh)] + [From Powerwall (kWh)]) / [Home (kWh)]
aggcalc.2.name: Year
aggcalc.2.expr: year(Date)
aggcalc.3.name: Month
aggcalc.3.expr: month(Date)

x: Month
y.0: Self-Powered
color: Year

xtick.count: 12

ytick.start: 0
ytick.end: 100
ytick.count: 11

precision: 1
datetime: Month
~~~


~~~ data-table
data.url: data/solar.csv

calc.0.name: Year
calc.0.expr: year([Date time])
calc.1.name: Month
calc.1.expr: month([Date time])

filter: [Date time] >= date(2020, 6, 1)

agg.category.0: Year
agg.category.1: Month
agg.measure.0.name: Avg. Home (kWh)
agg.measure.0.field: Home (kWh)
agg.measure.0.func: Average
agg.measure.1.name: Avg. Solar (kWh)
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Average
agg.measure.2.name: Avg. Powerwall (kWh)
agg.measure.2.field: From Powerwall (kWh)
agg.measure.2.func: Average
agg.measure.3.name: Avg. Grid (kWh)
agg.measure.3.field: From Grid (kWh)
agg.measure.3.func: Average

aggcalc.0.name: Avg. Solar (kWh)
aggcalc.0.expr: [Avg. Home (kWh)] - [Avg. Powerwall (kWh)] - [Avg. Grid (kWh)]
aggcalc.1.name: Self-Powered
aggcalc.1.expr: round(100 * ([Avg. Solar (kWh)] + [Avg. Powerwall (kWh)]) / [Avg. Home (kWh)], 0) + '%'

sort.0.field: Year
sort.0.desc: true
sort.1.field: Month
sort.1.desc: true

category.0: Year
category.1: Month
field.0: Self-Powered
field.1: Avg. Home (kWh)
field.2: Avg. Solar (kWh)
field.3: Avg. Powerwall (kWh)
field.4: Avg. Grid (kWh)

precision: 1
~~~
