[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
Table


# Monthly Table

~~~ data-table
data.url: data/solar.csv
data.join.0.url: data/hvac.csv
data.join.0.left: year([Date time]) + '-' + month([Date time])
data.join.0.right: year([Date]) + '-' + month([Date])
data.join.1.url: data/auto.csv
data.join.1.left: year([Date time]) + '-' + month([Date time])
data.join.1.right: year([Date]) + '-' + month([Date])

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
agg.measure.0.func: Sum
agg.measure.1.name: Solar (kWh)
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Sum
agg.measure.2.field: Home (kWh)
agg.measure.2.func: Sum
agg.measure.3.name: HVAC (kWh)
agg.measure.3.field: HVAC Total (kWh)
agg.measure.3.func: Average
agg.measure.4.name: Auto (kWh)
agg.measure.4.field: Auto Home (kWh)
agg.measure.4.func: Average

aggcalc.0.name: HVAC (kWh)
aggcalc.0.expr: if([HVAC (kWh)] == null, '', [HVAC (kWh)])
aggcalc.1.name: Auto (kWh)
aggcalc.1.expr: if([Auto (kWh)] == null, '', [Auto (kWh)])
aggcalc.2.name: Other (kWh)
aggcalc.2.expr: if([HVAC (kWh)] == '' && [Auto (kWh)] == '', '', [Home (kWh)] - [HVAC (kWh)] - [Auto (kWh)])
aggcalc.3.name: HVAC %
aggcalc.3.expr: if([HVAC (kWh)] == '', '', fixed(100 * [HVAC (kWh)] / [Home (kWh)], 1) + '%')
aggcalc.4.name: Auto %
aggcalc.4.expr: if([Auto (kWh)] == '', '', fixed(100 * [Auto (kWh)] / [Home (kWh)], 1) + '%')
aggcalc.5.name: Other %
aggcalc.5.expr: if([Other (kWh)] == '', '', fixed(100 * [Other (kWh)] / [Home (kWh)], 1) + '%')

sort.0.field: Year
sort.0.desc: true
sort.1.field: Month
sort.1.desc: true

category.0: Year

precision: 1
datetime: Month
~~~
