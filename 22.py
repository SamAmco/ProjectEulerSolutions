import re

def LetterScore(s):
	score = 0
	for c in s:
		score += ord(c.lower()) - 96
	return score

with open('p022_names.txt', 'r') as f:
	regex = re.compile(r'\w+')
	names = regex.findall(f.read())
	sortedNames = sorted(names)

	s = 0
	index = 1
	for name in sortedNames:
		s += LetterScore(name) * index
		index += 1

	print(s)