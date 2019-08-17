import sys, regex

word = ''
count = 0

for line in sys.stdin:
	line = regex.sub('[^\w\s]', "", line.split(',')[0])
	if (line):
		if (line == word):
			count += 1
		else:
			if (count > 0):
				print(word, count)
				count = 1
			word = line
