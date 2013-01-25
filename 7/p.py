import math

i = 2
count = 0

def isPrime(n):
	if n % 2 == 0:
		return False
	temp = math.ceil(math.sqrt(n)) + 1
	while temp > 1:
		if n % temp == 0:
			return False
		temp -= 1
	return True

while count != 10001:
	if(isPrime(i) == True):
		count += 1

	i += 1

print i - 1