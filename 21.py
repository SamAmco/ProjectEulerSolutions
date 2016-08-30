divisorSums = []
amicableNumbers = []

def d(x):
	s = 0
	for index in range(1, x):
		if (x % index == 0):
			s+=index
	return s


for index in range(10000):
	divisorSums.append(d(index))
	if (len(divisorSums) - 1 > divisorSums[index]):
		if (divisorSums[divisorSums[index]] == index):
			amicableNumbers.append(index)
			amicableNumbers.append(divisorSums[index])

s = 0
for i in amicableNumbers:
	s += i

print(s)
