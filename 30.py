import time

t = time.clock()

solSum = 0

for i in range(2, 354294):
	tempSum = 0
	for digit in str(i):
		tempSum += int(digit) ** 5
	if tempSum == i:
		solSum += tempSum

print solSum

print (time.clock() - t)