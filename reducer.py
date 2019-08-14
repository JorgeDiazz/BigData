import sys
import re

word1 = ''
count = 0

for line in sys.stdin:
	line = re.sub('[^\w\s]', "", line.split(',')[0])
	if(line != word1):
		if(count > 0):
			print(word1, count)
		word1 = line
		count = 1
	else:
		count += 1

	
