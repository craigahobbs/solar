[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md)


# Grid

~~~ data-table
data.url: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Year
aggregation.measures.0.field: From Grid (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: To Grid (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Grid Surplus (kWh)
aggregation.measures.2.function: Sum

sorts.0.field: YEAR(Date time)
sorts.0.desc: true

precision: 1
datetime: Year

categoryFields.0: YEAR(Date time)
fields.0: SUM(Grid Surplus (kWh))
fields.1: SUM(To Grid (kWh))
fields.2: SUM(From Grid (kWh))
~~~

~~~ line-chart
title: Grid Surplus (Monthly)
width: 900
height: 350

data.url: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: Grid Surplus (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: MONTH(Date time)
yFields.0: SUM(Grid Surplus (kWh))

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
title: To/From Grid
width: 1050
height: 350

data.url: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

precision: 1
datetime: Day

xField: Date time
yFields.0: From Grid (kWh)
yFields.1: To Grid (kWh)

yTicks.start.number: -80
yTicks.end.number: 80
yTicks.count: 9

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value.live.value: Year
~~~

~~~ line-chart
title: To/From Grid (Monthly)
width: 1100
height: 350

data.url: solar.csv

variables.start.live.value: Year
variables.start.live.index: -1
variables.end.live.value: Year
variables.end.live.index: 1

filters.0.field: Date time
filters.0.gte.variable: start
filters.0.lt.variable: end

aggregation.categories.0.field: Date time
aggregation.categories.0.by: Month
aggregation.measures.0.field: From Grid (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: To Grid (kWh)
aggregation.measures.1.function: Sum

precision: 1
datetime: Day

xField: MONTH(Date time)
yFields.0: SUM(From Grid (kWh))
yFields.1: SUM(To Grid (kWh))

yTicks.start.number: -1200
yTicks.end.number: 1200
yTicks.count: 9

xTicks.start.variable: start
xTicks.end.variable: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value.live.value: Year
~~~
