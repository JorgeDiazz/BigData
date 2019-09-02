import sys

cities_in_county1 = ''
county1 = ''
total_counties = 1

for line in sys.stdin:

	cities_in_county2 = cities_in_county1
	county2 = county1
	
	data = line.strip().split()

	cities_in_county1 = data[0]
	county1 = data[1]

	if(not county2):
		continue

	if(cities_in_county1 == cities_in_county2):
		total_counties += 1
	else:	
		print total_counties, cities_in_county2
		total_counties = 1


print total_counties, cities_in_county1


