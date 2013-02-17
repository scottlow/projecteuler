import math
from collections import *
import time

t = time.clock()

primeCount = 0

primeDict = {}

def findPrimes(n):
	primes = [True] * n
	for i in range(2, int(math.sqrt(n)) + 1):
		if primes[i] == True:
			j = i ** 2
			while j < n:
				primes[j] = False
				j += i

	for i in range(2, len(primes)):
		if primes[i] == True:
			primeDict[i] = 1

findPrimes(1000000)

for prime in primeDict:
	dq = deque(str(prime))
	combinations = []
	for i in range(len(dq)):
		dq.rotate(-1)
		combinations.append(''.join(dq))
	
	if all(int(combination) in primeDict for combination in combinations):
		primeCount += 1

print primeCount
print time.clock() - t
