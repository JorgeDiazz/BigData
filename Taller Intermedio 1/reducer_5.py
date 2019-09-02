import sys
from functools import reduce

transfer_year_1 = 0
transfer_month_1 = 0
months_counter = {}

for line in sys.stdin:

	transfer_year_2 = transfer_year_1
	transfer_month_2 = transfer_month_1

	data = line.strip().split()

	transfer_year_1 = int(data[0])
	transfer_month_1 = int(data[1])
	
	if (transfer_year_2 == 0):
		continue

	if (transfer_month_2 not in months_counter):
		months_counter[transfer_month_2] = 0

	if (transfer_year_1 == transfer_year_2):
		months_counter[transfer_month_2] = months_counter[transfer_month_2] + 1	
	else: 
		print transfer_year_2, max(months_counter, key=months_counter.get)
		months_counter = {}


if (transfer_month_1 not in months_counter):
		months_counter[transfer_month_1] = 0
months_counter[transfer_month_1] = months_counter[transfer_month_1] + 1

print transfer_year_1, max(months_counter, key=months_counter.get)