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

findPrimes(750000)

for prime in primeDict:
	num = str(prime)
	combinations = []
	for i in range(1, len(num)):
		combinations.append(num[i:])
		combinations.append(num[0:len(num) - i])

	if all(int(combination) in primeDict for combination in combinations):
		primeCount += prime

print primeCount - 17
print time.clock() - t
