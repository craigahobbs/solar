[Home](#url=README.md) |
[Solar](#url=solar.md) |
Grid |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Grid

~~~ data-table
data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Year
calculatedFields.0.expression: date(year([Date time]), 1, 1)
calculatedFields.1.name: Grid Surplus (kWh)
calculatedFields.1.expression: -[To Grid (kWh)] - [From Grid (kWh)]

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Year
aggregation.measures.0.field: From Grid (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: To Grid (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Grid Surplus (kWh)
aggregation.measures.2.function: Sum

sorts.0.field: Year
sorts.0.desc: true

precision: 1
datetime: Year

categoryFields.0: Year
fields.0: SUM(Grid Surplus (kWh))
fields.1: SUM(To Grid (kWh))
fields.2: SUM(From Grid (kWh))
~~~

~~~ line-chart
title: Grid Surplus (Monthly)
width: 900
height: 350

data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date time]), month([Date time]), 1)
calculatedFields.1.name: Grid Surplus (kWh)
calculatedFields.1.expression: -[To Grid (kWh)] - [From Grid (kWh)]

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Month
aggregation.measures.0.field: Grid Surplus (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(Grid Surplus (kWh))

yTicks.start: -1200
yTicks.end: 1200
yTicks.count: 9
yTicks.skip: 1

xTicks.start: start
xTicks.end: end
xTicks.count: 25
xTicks.skip: 3

yAnnotations.0.value: 0
yAnnotations.0.label: ''

xAnnotations.0.value: date(year(now()), 1, 1)
~~~

~~~ line-chart
title: To/From Grid
width: 1050
height: 350

data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

filters.0: ([Date time] >= start) && ([Date time] < end)

precision: 1
datetime: Day

xField: Date time
yFields.0: From Grid (kWh)
yFields.1: To Grid (kWh)

yTicks.start: -80
yTicks.end: 80
yTicks.count: 9

xTicks.start: start
xTicks.end: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value: date(year(now()), 1, 1)
~~~

~~~ line-chart
title: To/From Grid (Monthly)
width: 1100
height: 350

data.url: solar.csv

variables.start: date(year(now()) - 1, 1, 1)
variables.end: date(year(now()) + 1, 1, 1)

calculatedFields.0.name: Month
calculatedFields.0.expression: date(year([Date time]), month([Date time]), 1)

filters.0: ([Date time] >= start) && ([Date time] < end)

aggregation.categoryFields.0: Month
aggregation.measures.0.field: From Grid (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: To Grid (kWh)
aggregation.measures.1.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: SUM(From Grid (kWh))
yFields.1: SUM(To Grid (kWh))

yTicks.start: -1200
yTicks.end: 1200
yTicks.count: 9

xTicks.start: start
xTicks.end: end
xTicks.count: 25
xTicks.skip: 3

xAnnotations.0.value: date(year(now()), 1, 1)
~~~
