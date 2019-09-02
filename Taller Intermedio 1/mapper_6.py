import sys

COMMA_SEPARATOR = ','

for line in sys.stdin:

	data = line.strip()

	if(data):

		data = data.split(COMMA_SEPARATOR)

		city = data[6]
		county = data[8]

		price = data[1]

		if(price.isdigit()):
			print county, city