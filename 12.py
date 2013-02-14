import operator
import time

t = time.clock()

factors = {}
i = 0
count = 1
current = 1

def increment(x):
	if factors.get(x) == None:
		factors[x] = 2 # start at two for arithmetic later
	else:
		factors[x] += 1

def primeFactors(n):
	x = 2
	while(n > 1):
		while(n % x == 0):
			increment(x)
			n /= x
		x += 1

while True:
	factors = {}
	primeFactors(current)

	if reduce(operator.mul, factors.values(), 1) >= 500:
		print current
		break

	count += 1
	current += count

print "Time: %f"%(time.clock() - t)