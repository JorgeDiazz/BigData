import sys

for line in sys.stdin:
	words = line.split()
	for key in words:
	    print(key, 1)

