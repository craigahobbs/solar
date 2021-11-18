[Home](#url=README.md) |
[Monthly](#url=offset-monthly.md) |
[Yearly](#url=offset-yearly.md)


# Solar Offset (Yearly)

~~~ data-table
dataURL: solar.csv

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Year
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Solar Offset (kWh)
aggregation.measures.2.function: Sum

categoryFields.0: YEAR(Date time)
fields.0: SUM(Solar Offset (kWh))
fields.1: SUM(Solar Energy (kWh))
fields.2: SUM(Home (kWh))

sort.0.field: YEAR(Date time)
sort.0.desc: true

precision: 1
datetime: Year
~~~

~~~ line-chart
title: Solar Offset (Yearly)
width: 1024
height: 480

dataURL: solar.csv

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Year
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum

xField: YEAR(Date time)
yFields.0: SUM(Home (kWh))
yFields.1: SUM(Solar Energy (kWh))

precision: 1
datetime: Day

yTicks.start.number: 0
yTicks.end.number: 14000
yTicks.count: 15
yTicks.skip: 1

xTicks.count: 9
xTicks.skip: 1
~~~
