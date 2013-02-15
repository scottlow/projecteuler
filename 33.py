from fractions import *
import time

t = time.clock()

numProd = 1
denomProd = 1

for denom in range(99, 9, -1):
	for num in range(10, denom):

		testDenom = str(denom)[1]
		if '0' in testDenom:
			continue

		test = float(str(num)[0])/float(testDenom)
		
		if str(num)[1] == str(denom)[0] and test == float(num)/float(denom):
			numProd *= num
			denomProd *= denom

fraction = Fraction(numProd, denomProd)

print fraction

print (time.clock() - t)