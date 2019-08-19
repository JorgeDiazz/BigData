import sys

for line in sys.stdin:
	words = line.split()
	for key in words:
	    print("%s,%d" %(key,1))
