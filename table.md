[Home](#url=README.md) |
[Solar](#url=solar.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
Table


# Monthly Table

~~~ data-table
data.url: solar.csv
data.preCalculatedFields.0.name: Year
data.preCalculatedFields.0.expression: year([Date time])
data.preCalculatedFields.1.name: Month
data.preCalculatedFields.1.expression: month([Date time])

data.joins.0.url: hvac.csv
data.joins.0.leftFields.0: Year
data.joins.0.leftFields.1: Month
data.joins.0.preCalculatedFields.0.name: Year
data.joins.0.preCalculatedFields.0.expression: year([Date])
data.joins.0.preCalculatedFields.1.name: Month
data.joins.0.preCalculatedFields.1.expression: month([Date])

calculatedFields.0.name: Solar Offset (kWh)
calculatedFields.0.expression: [Solar Energy (kWh)] - [Home (kWh)]
calculatedFields.1.name: HVAC (kWh)
calculatedFields.1.expression: if([HVAC Total (kWh)] != null,[HVAC Total (kWh)],0)

filters.0: [Date time] >= date(2020, 6, 1)

aggregation.categoryFields.0: Year
aggregation.categoryFields.1: Month
aggregation.measures.0.field: Solar Offset (kWh)
aggregation.measures.0.function: Sum
aggregation.measures.1.field: Solar Energy (kWh)
aggregation.measures.1.function: Sum
aggregation.measures.2.field: Home (kWh)
aggregation.measures.2.function: Sum
aggregation.measures.3.field: HVAC (kWh)
aggregation.measures.3.function: Average

postCalculatedFields.0.name: HVAC %
postCalculatedFields.0.expression: if([AVERAGE(HVAC (kWh))] != 0,fixed(100 * [AVERAGE(HVAC (kWh))] / [SUM(Home (kWh))], 1) + '%', '')

sorts.0.field: Year
sorts.0.desc: true
sorts.1.field: Month
sorts.1.desc: true

precision: 1
datetime: Month

categoryFields.0: Year
~~~
