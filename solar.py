# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE

import argparse
import csv
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
        home_kwh = float(row['Home (kWh)'])
        solar_energy_kwh = float(row['Solar Energy (kWh)'])
        from_grid_kwh = float(row['From Grid (kWh)'])
        to_grid_kwh = float(row['To Grid (kWh)'])

        row['Solar Offset (kWh)'] = solar_energy_kwh - home_kwh
        row['Grid Surplus (kWh)'] = -to_grid_kwh - from_grid_kwh

    # Write the CSV
    writer = csv.DictWriter(sys.stdout, [
        'Date time',
        'Home (kWh)',
        'Solar Energy (kWh)',
        'From Powerwall (kWh)',
        'From Grid (kWh)',
        'To Grid (kWh)',
        'Solar Offset (kWh)',
        'Grid Surplus (kWh)'
    ])
    writer.writeheader()
    for row in data:
        writer.writerow(row)


######################################################################

if __name__ == '__main__':
    main()
