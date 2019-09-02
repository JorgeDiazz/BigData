import sys

SPACE_SEPARATOR = ' '

city2 = ''
minimum_city_price = sys.maxsize

for line in sys.stdin:

	line = line.strip()

	last_space_index = line.rfind(SPACE_SEPARATOR)

	city1 = line[:last_space_index]
	current_price = int(line[last_space_index:])

	if (city1 == city2):
		minimum_city_price = current_price if minimum_city_price > current_price else minimum_city_price 
	else:
		if (minimum_city_price < sys.maxsize):
			print "%s, %d" %(city2, minimum_city_price)
		minimum_city_price = current_price
		city2 = city1

print "%s, %d" %(city2, minimum_city_price)
