import sys


SPACE_SEPARATOR = ' '

county1 = ''
city1 = ''
city_counter = {}

for line in sys.stdin:

	county2 = county1
	city2 = city1

	data = line.strip().split()

	county1 = data[0]
	city1 = data[1]

	if (not county2):
		continue

	if(county2 not in city_counter):
		city_counter[county2] = 0
	city_counter[county2] = city_counter[county2] + 1


for county in city_counter:
	print city_counter[county], county