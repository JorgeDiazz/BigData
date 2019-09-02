import sys, re

COMMA_SEPARATOR = ','

for line in sys.stdin:

	data = re.sub(r'[^\w\s,]', "", line.strip())

	if(data):

		data = data.split(COMMA_SEPARATOR)
		price = data[1]
		city = data[6]

		if(price.isdigit()):
			print city, price