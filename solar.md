[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md)


# Solar

~~~ data-table
dataURL: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

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
title: Solar Offset (Monthly)
width: 900
height: 350

dataURL: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum

xField: MONTH(Date time)
yFields.0: SUM(Solar Offset (kWh))

precision: 1
datetime: Day

yTicks.start.number: -1200
yTicks.end.number: 1200
yTicks.count: 9
yTicks.skip: 1

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

yAnnotations.0.value.number: 0
yAnnotations.0.label:

xAnnotations.0.value.live.value: Year
~~~

~~~ line-chart
title: Solar and Home (Monthly)
width: 1100
height: 350

dataURL: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

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
datetime: Day

yTicks.start.number: 0
yTicks.end.number: 2500
yTicks.count: 11
yTicks.skip: 1

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value.live.value: Year
~~~

~~~ data-table
dataURL: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

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
