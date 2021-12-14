# Licensed under the MIT License
# https://github.com/craigahobbs/solar/blob/main/LICENSE


.PHONY: help
help:
	@echo "usage: make [data|help]"


.PHONY: data
data:
	cat `ls -1 data/*.csv | head -n 1` | head -n 1 > solar.csv
	for CSV in data/*.csv; do cat $$CSV | tail -n+2 >> solar.csv; done
