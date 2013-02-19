import time
import itertools
import math

t = time.clock()

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

findPrimes(10000)

for i in range (1, 6670):
	nums = [i, i + 3330, i + 3330 * 2]
	permutations = [int(''.join(perm)) for perm in itertools.permutations(str(i))]
	if all(num in primeDict and num in permutations and num != 1487 for num in nums):
		print ''.join(str(number) for number in nums)
		break

print time.clock() - t

