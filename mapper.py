import sys

for line in sys.stdin:
	words = line.lower().split()
	for key in words:
	    print(key)
