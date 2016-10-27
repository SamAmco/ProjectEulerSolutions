def GenDigits(x):
	while x > 0:
		r = divmod(x, 10)
		x = r[0]
		yield r[1]

s = 0
for x in range(2, 999999):
	results = GenDigits(x)
	accum = 0
	for y in results:
		accum += pow(y,5)
	if accum == x:
		s += x

print(s)