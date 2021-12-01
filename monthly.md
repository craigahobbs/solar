[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
Monthly |
[Table](#url=table.md)


# Monthly

~~~ line-chart
title: Monthly Solar Energy
width: 900
height: 350

data.url: solar.csv

filters.0.field: Date time
filters.0.gte.datetime: 2020-06-01

aggregation.categories.0.field: Year
aggregation.categories.1.field: Month
aggregation.measures.0.field: Solar Energy (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(Solar Energy (kWh))
colorFields.0: Year

yTicks.start.number: 0
yTicks.end.number: 2500
yTicks.count: 11
yTicks.skip: 1

xTicks.count: 12
~~~

~~~ line-chart
title: Monthly Power Usage
width: 900
height: 350

data.url: solar.csv

filters.0.field: Date time
filters.0.gte.datetime: 2020-06-01

aggregation.categories.0.field: Year
aggregation.categories.1.field: Month
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(Home (kWh))
colorFields.0: Year

yTicks.start.number: 0
yTicks.end.number: 1500
yTicks.count: 7

xTicks.count: 12
~~~

~~~ line-chart
title: Monthly Solar Offset
width: 900
height: 350

data.url: solar.csv

filters.0.field: Date time
filters.0.gte.datetime: 2020-06-01

aggregation.categories.0.field: Year
aggregation.categories.1.field: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(Solar Offset (kWh))
colorFields.0: Year

yTicks.start.number: -1000
yTicks.end.number: 1500
yTicks.count: 11
yTicks.skip: 1

xTicks.count: 12
~~~
