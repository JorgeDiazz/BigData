import sys

COMMA_SEPARATOR = ','
LINE_SEPARATOR = '-'

for line in sys.stdin:

	data = line.strip()

	if(data):

		data = data.split(COMMA_SEPARATOR)

		transfer_date = data[2]
		transfer_year = transfer_date[0 : transfer_date.find(LINE_SEPARATOR)]

		if(transfer_year.isdigit()):
			print transfer_year