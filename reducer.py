import sys, re

word2 = ''
count = 0

for word1 in sys.stdin:
	word1 = re.sub('[^\w\s]', "", word1.split(',')[0])
	if (word1):
		if (word1 == word2):
			count += 1
		else:
			if (count > 0):
				print(word2, count)
				count = 1
			word2 = word1
