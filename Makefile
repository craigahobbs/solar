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
data: data/solar.csv


data/solar.csv: data-raw/*.csv
	cat `ls -1 data-raw/*.csv | head -n 1` | head -n 1 > $@
	for CSV in data-raw/*.csv; do cat $$CSV | tail -n+2 >> $@; done
