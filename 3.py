def primeFactors(n):
	factors = []
	x = 2

	while(n > 1):
		while(n % x == 0):
			factors.append(x)
			n /= x
		x += 1

	return factors

print primeFactors(28)