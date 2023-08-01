# Licensed under the MIT License
# https://github.com/craigahobbs/solar/blob/main/LICENSE


.PHONY: help
help:
	@echo 'usage: make [data|help]'


.PHONY: clean
clean:


.PHONY: commit
commit:


.PHONY: gh-pages
gh-pages:


.PHONY: superclean
superclean:


.PHONY: data
data:
	python3 -c "$$DATA_JOIN"


define DATA_JOIN
import csv
import os

# Read all CSVs
all_rows = []
for csv_filename in sorted(os.listdir('data-raw')):
	csv_path = os.path.join('data-raw', csv_filename)
	with open(csv_path, 'r') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			all_rows.append(row)

			# Fix old file's "To Grid" value
			to_grid = float(row['To Grid (kWh)'])
			if to_grid < 0:
				row['To Grid (kWh)'] = -to_grid


# Write the complete CSV
with open('data/solar.csv', 'w', newline='') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=all_rows[0].keys())
	writer.writeheader()
	for row in all_rows:
		writer.writerow(row)
endef
export DATA_JOIN
