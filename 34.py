cache = {}
def factorial(a):
    if a not in cache:
        if a == 0:
            return 1
        if a == 1:
            return 1
        cache[a] = a * factorial(a-1)
    return cache[a]

answers = []
for i in range(10, 2540161):
    x, s = i, 0
    while(x > 0):
        s += factorial(x % 10)
        x //= 10
    if s == i:
        answers.append(i)

print(sum(answers))
