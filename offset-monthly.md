[Home](#url=README.md) |
[Monthly](#url=offset-monthly.md) |
[Yearly](#url=offset-yearly.md)


# Solar Offset (Monthly)

~~~ line-chart
title: Solar Offset (Monthly)
width: 900
height: 350

dataURL: solar.csv

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum

xField: MONTH(Date time)
yFields.0: SUM(Solar Offset (kWh))

precision: 1
datetime: Month

yTicks.start.number: -2000
yTicks.end.number: 2000
yTicks.count: 9
yTicks.skip: 1

xTicks.start.datetime: 2020-01-01
xTicks.end.datetime: 2022-01-01
xTicks.count: 25
xTicks.skip: 2
~~~

~~~ line-chart
title: Solar and Home (Monthly)
width: 1100
height: 350

dataURL: solar.csv

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum

xField: MONTH(Date time)
yFields.0: SUM(Home (kWh))
yFields.1: SUM(Solar Energy (kWh))

precision: 1
datetime: Month

yTicks.start.number: 0
yTicks.end.number: 2500
yTicks.count: 11
yTicks.skip: 1

xTicks.start.datetime: 2020-01-01
xTicks.end.datetime: 2022-01-01
xTicks.count: 25
xTicks.skip: 2
~~~

~~~ data-table
dataURL: solar.csv

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Solar Offset (kWh)
aggregation.measures.2.function: Sum

categoryFields.0: MONTH(Date time)
fields.0: SUM(Solar Offset (kWh))
fields.1: SUM(Solar Energy (kWh))
fields.2: SUM(Home (kWh))

sort.0.field: MONTH(Date time)
sort.0.desc: true

precision: 1
datetime: Month
~~~
