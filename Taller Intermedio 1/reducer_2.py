import sys

SPACE_SEPARATOR = ' '

city2 = ''
city_counter = 0
total_city_prices = 0

for line in sys.stdin:

	line = line.strip()

	last_space_index = line.rfind(SPACE_SEPARATOR)

	city1 = line[:last_space_index]
	current_price = float(line[last_space_index:])

	if (city1 == city2):
		total_city_prices += current_price
		city_counter += 1
	else:
		if (total_city_prices > 0):
			print "%s, %f" %(city2, total_city_prices / city_counter)
		total_city_prices = current_price
		city2 = city1
		city_counter = 1

print "%s, %f" %(city2, total_city_prices / city_counter)
