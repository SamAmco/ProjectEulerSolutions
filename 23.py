
def IsAbundant(i):
	s = 0
	for x in range(1, (i // 2) + 1):
		if (i % x == 0):
			s += x
	return s > i

abundantNums = []
#find all abundant numbers between 12 (inclusive) and 28123 - 12 (inclusive)
for i in range(12,  28123 - 11):
	if (IsAbundant(i)):
		abundantNums.append(i)

abundantSums = []
#find the set of all numbers which are the sums of two abundant numbers
p1 = 0
p2 = 0
while p1 < len(abundantNums):
	while p2 < len(abundantNums):
		x = abundantNums[p1] + abundantNums[p2]
		if x > 28123:
			break
		else: abundantSums.append(abundantNums[p1] + abundantNums[p2])
		p2 += 1
	p1 += 1
	p2 = 0

cumulativeSum = 0
for i in range(1, 28123 + 1):
	if i not in abundantSums:
		cumulativeSum += i

print(cumulativeSum)

