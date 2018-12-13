numProd = 1
denomProd = 1
for x in range(1, 100):
    for y in range(x+1, 100):
        tl = x // 10
        tr = x % 10
        bl = y // 10
        br = y % 10
        if br != 0 and tr == bl and tl / br == x / y:
            numProd *= x
            denomProd *= y

print(str(numProd) + " / " + str(denomProd))
