import sys, re

word2 = ''
count = 0

for word1 in sys.stdin:
	word1 = word1.strip()
	if (word1):
		if (word1 == word2):
			count += 1
		else:
			if (count > 0):
				print "%s, %d" %(word2, count)
			count = 1
			word2 = word1

print "%s, %d" %(word2, count)