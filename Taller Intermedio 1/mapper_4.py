import sys, re

COMMA_SEPARATOR = ','
LINE_SEPARATOR = '-'

for line in sys.stdin:

	data = line.strip()

	if(data):

		data = data.split(COMMA_SEPARATOR)

		price = data[1]

		transfer_date = data[2].strip()
		transfer_year = transfer_date[0 : transfer_date.find(LINE_SEPARATOR)].strip()

		city = data[6]

		if(price.isdigit() and city == 'STAMFORD' and transfer_year == '2015'):
			print price