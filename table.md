[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
Table


# Monthly Table

~~~ data-table
data.url: solar.csv
data.join.0.url: hvac.csv
data.join.0.left: year([Date time]) + '-' + month([Date time])
data.join.0.right: year([Date]) + '-' + month([Date])
data.join.1.url: auto.csv
data.join.1.left: year([Date time]) + '-' + month([Date time])
data.join.1.right: year([Date]) + '-' + month([Date])

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
agg.measure.1.field: Solar Energy (kWh)
agg.measure.1.func: Sum
agg.measure.2.field: Home (kWh)
agg.measure.2.func: Sum
agg.measure.3.field: HVAC Total (kWh)
agg.measure.3.func: Average
agg.measure.4.field: Auto Total (kWh)
agg.measure.4.func: Average

aggcalc.0.name: HVAC %
aggcalc.0.expr: if([HVAC Total (kWh)] != null,fixed(100 * [HVAC Total (kWh)] / [Home (kWh)], 1) + '%', '')
aggcalc.1.name: Auto %
aggcalc.1.expr: if([Auto Total (kWh)] != null,fixed(100 * [Auto Total (kWh)] / [Home (kWh)], 1) + '%', '')

sort.0.field: Year
sort.0.desc: true
sort.1.field: Month
sort.1.desc: true

category.0: Year

precision: 1
datetime: Month
~~~
