import sys

COMMA_SEPARATOR = ','
LINE_SEPARATOR = '-'

for line in sys.stdin:

	data = line.strip()

	if(data):

		data = data.split(COMMA_SEPARATOR)

		transfer_date = data[2].split(LINE_SEPARATOR)
		transfer_year = transfer_date[0]

		if(transfer_year.isdigit()):

			transfer_month = transfer_date[1]
			
			print transfer_year, transfer_month