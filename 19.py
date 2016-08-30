from datetime import timedelta, date

def daterange(start, end):
	for n in range(int((end - start).days)):
		yield start + timedelta(n)

start = date(1901, 1, 1)
end = date(2000, 12, 31)
sum = 0
for day in daterange(start, end):
	if (day.weekday() == 6 and day.day == 1):
		sum += 1

print(sum)