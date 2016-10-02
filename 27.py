import sys, math

primeCache = [3]

def IsPrime(x):
	for i in range(2, int(math.sqrt(math.fabs(x))) + 1):
		if x % i == 0:
			return False;
	return True

def IsPrimeCached(x):
	global primeCache
	if primeCache[-1] < x:
		i = primeCache[-1]
		while primeCache[-1] < x:
			i += 1
			if IsPrime(i):
				primeCache.append(i)
				if x == i:
					return True
		return False
	elif primeCache[0] > x:
		i = primeCache[0]
		while primeCache[0] > x:
			i -= 1
			if IsPrime(i):
				primeCache = [i] + primeCache
				if x == i:
					return True
		return False
	elif x in primeCache:
		return True
	else: return False

def PrimeChainLength(a, b):
	i = 0
	while IsPrimeCached(math.pow(i, 2) + (a * i) + b):
		i += 1
	return i

for i in range(-1000, 1001):
	IsPrimeCached(i)

bPrimes = primeCache[:]

bInd = 0
b = bPrimes[0]
longestPair = (0,0)
longestChain = 0
while b <= 1000:
	for a in range(-999,1000):
		length = PrimeChainLength(a, b)
		if length > longestChain:
			longestChain = length
			longestPair = (a, b)
	bInd += 1
	b = bPrimes[bInd]

print(longestPair[0] * longestPair[1])

