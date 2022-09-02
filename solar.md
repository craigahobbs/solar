[Home](#url=README.md) |
Solar |
[Self-Powered](#url=self-powered.md) |
[Grid](#url=grid.md) |
[Powerwall](#url=powerwall.md) |
[Monthly](#url=monthly.md) |
[Table](#url=table.md)


# Solar Energy Generated and Power Used

~~~ markdown-script
# Load the daily solar data
data = dataParseCSV(fetch('data/solar.csv', null, true))

# Compute the x-axis extents
maxDateData = dataAggregate(data, objectNew( \
    'measures', arrayNew( \
        objectNew('field', 'Date time', 'function', 'max') \
    ) \
))
maxDate = objectGet(arrayGet(maxDateData, 0), 'Date time')
start = datetimeNew(datetimeYear(maxDate) - 1, 1, 1)
end = datetimeNew(datetimeYear(maxDate), datetimeMonth(maxDate), 1)

# Add calculated fields
dataCalculatedField(data, 'Month', 'date(year([Date time]), month([Date time]), 1)')
dataCalculatedField(data, 'Year', 'year([Date time])')
dataCalculatedField(data, 'Solar Offset (kWh)', '[Solar Energy (kWh)] - [Home (kWh)]')

# Compute total monthly home energy usage and solar power generation
monthly = dataAggregate(data, objectNew( \
    'categories', arrayNew('Month'), \
    'measures', arrayNew( \
        objectNew('field', 'Home (kWh)', 'function', 'sum'), \
        objectNew('field', 'Solar Energy (kWh)', 'function', 'sum') \
    ) \
))
monthly = dataFilter(monthly, 'Month >= start', objectNew('start', start))

# Compute the total annual home energy usage, solar energy generation, and solar offset
yearly = dataAggregate(data, objectNew( \
    'categories', arrayNew('Year'), \
    'measures', arrayNew( \
        objectNew('field', 'Home (kWh)', 'function', 'sum'), \
        objectNew('field', 'Solar Energy (kWh)', 'function', 'sum'), \
        objectNew('field', 'Solar Offset (kWh)', 'function', 'sum') \
    ) \
))
dataSort(yearly, arrayNew(arrayNew('Year', true)))

# Draw the monthly line chart
xtickCount = (12 * (datetimeYear(end) - datetimeYear(start)) - datetimeMonth(start)) + datetimeMonth(end) + 1
dataLineChart(monthly, objectNew( \
    'width', 1100, \
    'height', 350, \
    'x', 'Month', \
    'y', arrayNew('Home (kWh)', 'Solar Energy (kWh)'), \
    'precision', 1, \
    'datetime', 'month', \
    'xtick', objectNew( \
        'start', start, \
        'end', end, \
        'count', xtickCount, \
        'skip', 2 \
    ), \
    'ytick', objectNew( \
        'start', 0, \
        'end', 2500, \
        'count', 11, \
        'skip', 1 \
    ), \
    'xline', arrayNew(objectNew('value', datetimeNew(datetimeYear(end), 1, 1))) \
))

# Render the total annual table
dataTable(yearly, objectNew('precision', 1))
~~~
