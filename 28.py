

step = 2
countDown = 4
num = 1
cumulation = 0

while step < 1001:
	cumulation += num
	num += step
	countDown -= 1
	if countDown == 0:
		countDown = 4
		step += 2

cumulation += num
print(cumulation)