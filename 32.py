import time

t = time.clock()

products = {}

def isPandigital(i, j):
	number = str(i) + str(j) + str(i*j)
	if len(number) != 9 or '0' in number:
		return 0
	else:
		digits = {}
		for digit in number:
			if digit not in digits:
				digits[digit] = 1
			else:
				return 0

	return i*j

# BOUND OPTIMIZATION

# A 4 digit number * 1 digit number can yield a 4-5 digit product = 9 digits in total (could be 1-9 pandigital)
# 	Thus we require that one of the loops cycles through all possible 4 digit numbers

# A 3 digit number * 2 digit number can yield a 4-5 digit product = 9-10 digits in total (could be 1-9 pandidtal)
# 	Thus we require that the other loop cycles through all possible 2 digit numbers (since the outer loop already cycles through all possible 3 digit numbers)
# 
# This could still be refined further.

for i in range (1, 9999):
	for j in range (1, 99):
		temp = isPandigital(i, j)
		if temp == 0:
			continue
		else:
			if temp not in products:
				print i, j, temp
				products[temp] = 1

print sum(products.keys())

print (time.clock() - t)