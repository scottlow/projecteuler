import time

t = time.clock()

decimals = []
product = 1

for i in range(1, 1000000):
	decimals.append(str(i))

stringDec = ''.join(decimals)

for i in range(0, 7):
	product *= int(stringDec[(10**i) - 1])

print product
print time.clock() - t

