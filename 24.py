def createNumber(arr):
	ans = 0
	for n in arr:
		ans = (ans * 10) + n
	return ans

def findCombinations(arr, leftSide, rightSide):
	if (len(rightSide) == 0):
		return arr.append(leftSide)
	for i in range(0, len(rightSide)):
		nextPerms = findCombinations(arr, leftSide + [rightSide[i]], rightSide[0:i] + rightSide[(i+1):])
	return arr

numbers = [0,1,2,3,4,5,6,7,8,9]
print(createNumber(findCombinations([], [], numbers)[1000000-1]))