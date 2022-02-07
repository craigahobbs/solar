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

data.url: solar.csv

calculatedFields.0.name: Year
calculatedFields.0.expression: year([Date time])
calculatedFields.1.name: Month
calculatedFields.1.expression: month([Date time])

filter: [Date time] >= date(2020, 6, 1)

aggregation.categoryFields.0: Year
aggregation.categoryFields.1: Month
aggregation.measures.0.field: Solar Energy (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: Solar Energy (kWh)
colorField: Year

yTicks.start: 0
yTicks.end: 2500
yTicks.count: 11
yTicks.skip: 1

xTicks.count: 12
~~~

~~~ line-chart
title: 'Monthly Power Usage'
width: 900
height: 350

data.url: solar.csv

calculatedFields.0.name: Year
calculatedFields.0.expression: year([Date time])
calculatedFields.1.name: Month
calculatedFields.1.expression: month([Date time])

filter: [Date time] >= date(2020, 6, 1)

aggregation.categoryFields.0: Year
aggregation.categoryFields.1: Month
aggregation.measures.0.field: Home (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: Home (kWh)
colorField: Year

yTicks.start: 0
yTicks.end: 1500
yTicks.count: 7

xTicks.count: 12
~~~

~~~ line-chart
title: 'Monthly Solar Offset'
width: 900
height: 350

data.url: solar.csv

calculatedFields.0.name: Year
calculatedFields.0.expression: year([Date time])
calculatedFields.1.name: Month
calculatedFields.1.expression: month([Date time])
calculatedFields.2.name: Solar Offset (kWh)
calculatedFields.2.expression: [Solar Energy (kWh)] - [Home (kWh)]

filter: [Date time] >= date(2020, 6, 1)

aggregation.categoryFields.0: Year
aggregation.categoryFields.1: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum

precision: 1
datetime: Day

xField: Month
yFields.0: Solar Offset (kWh)
colorField: Year

yTicks.start: -1000
yTicks.end: 1500
yTicks.count: 11
yTicks.skip: 1

xTicks.count: 12

yAnnotations.0.value: 0
yAnnotations.0.label: ''
~~~
