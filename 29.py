import math

cache = []
dupCount = 0
gridSize = 100 + 1
for a in range(2, gridSize):
	for b in range(2, gridSize):
		if ((a, b) in cache):
			continue
		for c in range(a+1, gridSize):
			for d in range(2, gridSize):
				if (math.isclose(d / math.log(a, c), b)):
					dupCount += 1
					cache.append((c, d))

print(((gridSize - 2) * (gridSize - 2)) - dupCount)
