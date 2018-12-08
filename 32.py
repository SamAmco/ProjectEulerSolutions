import numpy as np

digits = np.arange(1,10)

def isPandigitalProduct(a, b, c):
    numbers = str(a) + str(b) + str(c)
    return all(str(x) in numbers for x in digits)


products = []
for multiplicand in range(0, 10000):
    for multiplier in range(multiplicand, 10000):
        product = multiplicand * multiplier
        if  len(str(multiplicand) + str(multiplier) + str(product)) > 9:
            break
        if isPandigitalProduct(multiplicand, multiplier, product):
            print('%s * %s = %s' % (multiplicand, multiplier, product))
            products.append(product)


print(sum(set(products)))
