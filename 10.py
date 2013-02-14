import math as m

def primeFactors(n):
	primes = [True] * n
	for i in range (2, int(m.sqrt(n))):
		if primes[i] is True:
			j = i ** 2
			while j < n:
				primes[j] = False
				j = j + i
	
	sum = 0

	for i in range(2, len(primes)):
		if primes[i] == True:
			sum += i

	return sum
print primeFactors(2000000)