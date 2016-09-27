def ReciprocalCycles(denominator):
	previousRemainders = []
	remainder = 1
	recipCycles = 0
	#see how many times the denominator goes into currentNum
	while(True):
		while (denominator > remainder):
			remainder *= 10
		remainder = remainder % denominator
		if remainder == 0:
			break
		elif remainder in previousRemainders:
			recipCycles = (len(previousRemainders) 
				- previousRemainders.index(remainder))
			break
		previousRemainders.append(remainder)
	return recipCycles


largest = 0
largestInd = 0
for i in range(1, 1000):
	c = ReciprocalCycles(i)
	if c > largest:
		largest = c
		largestInd = i
print(largestInd)
