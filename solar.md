~~~ markdown-script
# Licensed under the MIT License
# https://github.com/craigahobbs/solar/blob/main/LICENSE


async function solarMain()
    # Render the menu
    markdownPrint('[Home](#url=README.md&var=)')
    curPage = null
    for page, ixPage in arrayNew( \
        objectNew('fn', solarSolar, 'name', 'Solar', 'title', 'Solar Energy Generated and Power Used'), \
        objectNew('fn', solarSelfPowered, 'name', 'Self-Powered', 'title', 'Self-Powered by Month'), \
        objectNew('fn', solarGrid, 'name', 'Grid', 'title', 'Grid'), \
        objectNew('fn', solarPowerwall, 'name', 'Powerwall', 'title', 'Powerwall'), \
        objectNew('fn', solarMonthly, 'name', 'Monthly', 'title', 'Monthly'), \
        objectNew('fn', solarMonthlyTable, 'name', 'Table', 'title', 'Monthly Table') \
    ):
        pageName = objectGet(page, 'name')
        if vPage == pageName || (vPage == null && ixPage == 0):
            curPage = page
            markdownPrint('| ' + markdownEscape(pageName))
        else:
            markdownPrint('| [' + markdownEscape(pageName) + "](#var.vPage='" + urlEncodeComponent(pageName) + \
                if(vYears != null, "'&var.vYears=" + vYears, "'") + ')')
        endif
    endfor

    # Set the title
    curPageTitle = objectGet(curPage, 'title')
    markdownPrint('', '# ' + curPageTitle, '')
    documentSetTitle(curPageTitle)

    # Render the page
    curPageFn = objectGet(curPage, 'fn')
    curPageFn()
endfunction


# Chart size constants
solarChartWidthWide = 1100
solarChartWidth = 900
solarChartHeight = 350


async function solarSolar()
    # Load the solar data
    solarData = solarLoadData()
    monthly = objectGet(solarData, 'monthly')
    yearly = objectGet(solarData, 'yearly')
    curYear = objectGet(solarData, 'curYear')

    # Draw the monthly solar energy line chart

    dataLineChart(monthly, objectNew( \
        'width', solarChartWidthWide, \
        'height', solarChartHeight, \
        'x', 'Date', \
        'y', arrayNew('Home (kWh)', 'Solar Energy (kWh)'), \
        'datetime', 'month', \
        'xTicks', objectNew( \
            'count', arrayLength(monthly), \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'start', 0, \
            'end', 2500, \
            'count', 11, \
            'skip', 1 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', curYear, 'label', datetimeISOFormat(curYear, true)) \
        ) \
    ))

    # Render the total annual solar energy table
    dataSort(yearly, arrayNew(arrayNew('Year', true)))
    dataTable(yearly, objectNew( \
        'categories', arrayNew('Year'), \
        'fields', arrayNew( \
            'Solar Offset (kWh)', \
            'Solar Energy (kWh)', \
            'Home (kWh)' \
        ), \
        'precision', 1 \
    ))
endfunction


async function solarSelfPowered()
    # Load the solar data
    solarData = solarLoadData('average')
    monthly = objectGet(solarData, 'monthly')

    # Compute the monthly self-powered percentage
    dataCalculatedField(monthly, 'From Solar (kWh)', '[Home (kWh)] - [From Powerwall (kWh)] - [From Grid (kWh)]')
    dataCalculatedField(monthly, 'Self-Powered%', '100 * ([From Solar (kWh)] + [From Powerwall (kWh)]) / [Home (kWh)]')

    # Draw the monthly self-powered line chart
    dataLineChart(monthly, objectNew( \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Month', \
        'y', arrayNew('Self-Powered%'), \
        'color', 'Year', \
        'xTicks', objectNew('count', 12), \
        'yTicks', objectNew('count', 11, 'skip', 1, 'start', 0, 'end', 100) \
    ))

    # Render the monthly self-powered table
    dataSort(monthly, arrayNew(arrayNew('Year', true), arrayNew('Month', true)))
    dataTable(monthly, objectNew( \
        'categories', arrayNew('Year', 'Month'), \
        'fields', arrayNew( \
            'Self-Powered%', \
            'Home (kWh)', \
            'Solar Energy (kWh)', \
            'From Powerwall (kWh)', \
            'From Grid (kWh)' \
        ), \
        'precision', 1 \
    ))
endfunction


async function solarGrid()
    # Load the solar data
    solarData = solarLoadData()
    data = objectGet(solarData, 'data')
    monthly = objectGet(solarData, 'monthly')
    yearly = objectGet(solarData, 'yearly')
    curYear = objectGet(solarData, 'curYear')

    # Calcuate the grid surplus
    dataCalculatedField(monthly, 'Grid Surplus (kWh)', '[To Grid (kWh)] - [From Grid (kWh)]')
    dataCalculatedField(yearly, 'Grid Surplus (kWh)', '[To Grid (kWh)] - [From Grid (kWh)]')

    # Draw the monthly grid surplus line chart
    dataLineChart(monthly, objectNew( \
        'title', 'Grid Surplus (Monthly)', \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Date', \
        'y', arrayNew('Grid Surplus (kWh)'), \
        'datetime', 'month', \
        'xTicks', objectNew( \
            'count', arrayLength(monthly), \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'start', -1200, \
            'end', 1200, \
            'count', 9 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', curYear, 'label', datetimeISOFormat(curYear, true)) \
        ), \
        'yLines', arrayNew( \
            objectNew('value', 0, 'label', '') \
        ) \
    ))

    # Render the annual grid surplus table
    dataSort(yearly, arrayNew(arrayNew('Year', true)))
    dataTable(yearly, objectNew( \
        'fields', arrayNew( \
            'Year', \
            'Grid Surplus (kWh)', \
            'To Grid (kWh)', \
            'From Grid (kWh)' \
        ), \
        'precision', 1, \
        'datetime', 'year' \
    ))

    # Draw the hourly to/from grid line chart
    dataLineChart(data, objectNew( \
        'title', 'To/From Grid', \
        'width', solarChartWidthWide, \
        'height', solarChartHeight, \
        'x', 'Date time', \
        'y', arrayNew('From Grid (kWh)', 'To Grid (kWh)'), \
        'datetime', 'day', \
        'xTicks', objectNew( \
            'count', 6 \
        ), \
        'yTicks', objectNew( \
            'start', -80, \
            'end', 120, \
            'count', 6 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', curYear, 'label', datetimeISOFormat(curYear, true)) \
        ) \
    ))

    # Draw the monthly to/from grid line chart
    dataLineChart(monthly, objectNew( \
        'title', 'To/From Grid (Monthly)', \
        'width', solarChartWidthWide, \
        'height', solarChartHeight, \
        'x', 'Date', \
        'y', arrayNew('From Grid (kWh)', 'To Grid (kWh)'), \
        'datetime', 'month', \
        'xTicks', objectNew( \
            'count', arrayLength(monthly), \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'start', 0, \
            'end', 1200, \
            'count', 9 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', curYear, 'label', datetimeISOFormat(curYear, true)) \
        ) \
    ))
endfunction


async function solarPowerwall()
    # Load the solar data
    solarData = solarLoadData('average')
    data = objectGet(solarData, 'data')
    monthly = objectGet(solarData, 'monthly')
    curYear = objectGet(solarData, 'curYear')

    # Draw the monthly from-powerwall line chart
    dataLineChart(monthly, objectNew( \
        'title', 'Average From Powerwall (Monthly)', \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Date', \
        'y', arrayNew('From Powerwall (kWh)'), \
        'datetime', 'month', \
        'xTicks', objectNew( \
            'count', arrayLength(monthly), \
            'skip', 2 \
        ), \
        'yTicks', objectNew( \
            'start', 0, \
            'end', 30, \
            'count', 4 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', curYear, 'label', datetimeISOFormat(curYear, true)) \
        ) \
    ))

    # Draw the monthly from-powerwall line chart
    dataLineChart(data, objectNew( \
        'title', 'From Powerwall', \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Date time', \
        'y', arrayNew('From Powerwall (kWh)'), \
        'datetime', 'day', \
        'xTicks', objectNew( \
            'count', 6 \
        ), \
        'yTicks', objectNew( \
            'start', 0, \
            'end', 50, \
            'count', 6 \
        ), \
        'xLines', arrayNew( \
            objectNew('value', curYear, 'label', datetimeISOFormat(curYear, true)) \
        ) \
    ))
endfunction


async function solarMonthly()
    # Load the solar data
    solarData = solarLoadData()
    monthly = objectGet(solarData, 'monthly')

    # Draw the monthly solar energy line chart
    dataLineChart(monthly, objectNew( \
        'title', 'Solar Energy (Monthly)', \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Month', \
        'y', arrayNew('Solar Energy (kWh)'), \
        'color', 'Year', \
        'xTicks', objectNew( \
            'count', 12 \
        ), \
        'yTicks', objectNew( \
            'start', 0, \
            'end', 2500, \
            'count', 11, \
            'skip', 1 \
        ) \
    ))

    # Draw the monthly home energy usage line chart
    dataLineChart(monthly, objectNew( \
        'title', 'Home Energy Usage (Monthly)', \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Month', \
        'y', arrayNew('Home (kWh)'), \
        'color', 'Year', \
        'xTicks', objectNew( \
            'count', 12 \
        ), \
        'yTicks', objectNew( \
            'start', 0, \
            'end', 1500, \
            'count', 7 \
        ) \
    ))

    # Draw the monthly solar offet line chart
    dataLineChart(monthly, objectNew( \
        'title', 'Solar Offset (Monthly)', \
        'width', solarChartWidth, \
        'height', solarChartHeight, \
        'x', 'Month', \
        'y', arrayNew('Solar Offset (kWh)'), \
        'color', 'Year', \
        'xTicks', objectNew( \
            'count', 12 \
        ), \
        'yTicks', objectNew( \
            'start', -1000, \
            'end', 1500, \
            'count', 11, \
            'skip', 1 \
        ) \
    ))
endfunction


async function solarMonthlyTable()
    # Load the solar data
    solarData = solarLoadData()
    monthly = objectGet(solarData, 'monthly')

    # Join the hvac and auto data tables
    monthly = dataJoin(monthly, dataParseCSV(httpFetch('data/auto.csv', null, true)), 'Date')
    monthly = dataJoin(monthly, dataParseCSV(httpFetch('data/hvac.csv', null, true)), 'Date')

    # Add calculated fields
    dataCalculatedField(monthly, 'HVAC (kWh)', 'if([HVAC Total (kWh)] == null, "", [HVAC Total (kWh)])')
    dataCalculatedField(monthly, 'Auto (kWh)', 'if([Auto Home (kWh)] == null, "", [Auto Home (kWh)])')
    dataCalculatedField(monthly, 'Other (kWh)', 'if([HVAC (kWh)] == "" && [Auto (kWh)] == "", "", [Home (kWh)] - [HVAC (kWh)] - [Auto (kWh)])')
    dataCalculatedField(monthly, 'HVAC %', 'if([HVAC (kWh)] == "", "", fixed(100 * [HVAC Total (kWh)] / [Home (kWh)], 1) + "%")')
    dataCalculatedField(monthly, 'Auto %', 'if([Auto (kWh)] == "", "", fixed(100 * [Auto (kWh)] / [Home (kWh)], 1) + "%")')
    dataCalculatedField(monthly, 'Other %', 'if([Other (kWh)] == "", "", fixed(100 * [Other (kWh)] / [Home (kWh)], 1) + "%")')

    # Render the monthly data table
    dataSort(monthly, arrayNew(arrayNew('Year', true), arrayNew('Month', true)))
    dataTable(monthly, objectNew( \
        'categories', arrayNew('Year', 'Month'), \
        'fields', arrayNew( \
            'Solar Offset (kWh)', \
            'Solar Energy (kWh)', \
            'Home (kWh)', \
            'HVAC (kWh)', \
            'Auto (kWh)', \
            'Other (kWh)', \
            'HVAC %', \
            'Auto %', \
            'Other %' \
        ), \
        'precision', 1 \
    ))

endfunction


async function solarLoadData(aggFn)
    aggFn = if(aggFn != null, aggFn, 'sum')

    # Load the daily solar data
    data = dataParseCSV(httpFetch('data/solar.csv', null, true))

    # Compute the end date and the number of years to display
    maxDateData = dataAggregate(data, objectNew( \
        'measures', arrayNew( \
            objectNew('field', 'Date time', 'function', 'max') \
        ) \
    ))
    maxDate = objectGet(arrayGet(maxDateData, 0), 'Date time')
    endDate = datetimeNew(datetimeYear(maxDate), datetimeMonth(maxDate), 1)
    nYears = if(vYears != null, vYears, if(datetimeMonth(endDate) < 4, 2, 1))

    # Filter the data, if necessary
    if nYears > 0:
        minDate = datetimeNew(datetimeYear(maxDate) - nYears, 1, 1)
        data = dataFilter(data, '[Date time] >= minDate', objectNew('minDate', minDate))
    endif

    # Add calculated fields
    dataCalculatedField(data, 'Date', 'date(year([Date time]), month([Date time]), 1)')
    dataCalculatedField(data, 'Month', 'month([Date time])')
    dataCalculatedField(data, 'Year', 'year([Date time])')
    dataCalculatedField(data, 'Solar Offset (kWh)', '[Solar Energy (kWh)] - [Home (kWh)]')

    # Compute monthly aggregates
    aggMeasures = arrayNew( \
        objectNew('field', 'Home (kWh)', 'function', aggFn), \
        objectNew('field', 'Solar Energy (kWh)', 'function', aggFn), \
        objectNew('field', 'From Powerwall (kWh)', 'function', aggFn), \
        objectNew('field', 'From Grid (kWh)', 'function', aggFn), \
        objectNew('field', 'To Grid (kWh)', 'function', aggFn), \
        objectNew('field', 'Solar Offset (kWh)', 'function', aggFn) \
    )
    monthly = dataAggregate(data, objectNew( \
        'categories', arrayNew('Date', 'Month', 'Year'), \
        'measures', aggMeasures \
    ))

    # Compute annual aggregates
    yearly = dataAggregate(data, objectNew( \
        'categories', arrayNew('Year'), \
        'measures', aggMeasures \
    ))

    return objectNew( \
        'data', data, \
        'monthly', monthly, \
        'yearly', yearly, \
        'curYear', datetimeNew(datetimeYear(maxDate), 1, 1) \
    )
endfunction


solarMain()
~~~
