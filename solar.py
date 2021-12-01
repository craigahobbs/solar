# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE

import argparse
import csv
from datetime import datetime
import sys


def main():
    # Command line arguments
    parser = argparse.ArgumentParser(description='Consolodate solar energy data files')
    parser.add_argument('files', metavar='csv', nargs='+', help='A CSV data file')
    args = parser.parse_args()

    # Consolodate the raw data files
    data = []
    for filename in args.files:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data.extend(row for row in csv_reader)

    # Sort the data
    data = sorted(data, key=lambda row: row['Date time'])

    # Add solar offset field
    for row in data:
        date_time = datetime.fromisoformat(row['Date time'])
        home_kwh = float(row['Home (kWh)'])
        solar_energy_kwh = float(row['Solar Energy (kWh)'])
        from_grid_kwh = float(row['From Grid (kWh)'])
        to_grid_kwh = float(row['To Grid (kWh)'])

        row['Solar Offset (kWh)'] = round(solar_energy_kwh - home_kwh, 3)
        row['Grid Surplus (kWh)'] = round(-to_grid_kwh - from_grid_kwh, 3)
        row['Year'] = date_time.year
        row['Month'] = date_time.month

    # Write the CSV
    writer = csv.DictWriter(sys.stdout, [
        'Date time',
        'Home (kWh)',
        'Solar Energy (kWh)',
        'From Powerwall (kWh)',
        'From Grid (kWh)',
        'To Grid (kWh)',
        'Solar Offset (kWh)',
        'Grid Surplus (kWh)',
        'Year',
        'Month'
    ])
    writer.writeheader()
    for row in data:
        writer.writerow(row)


######################################################################

if __name__ == '__main__':
    main()
