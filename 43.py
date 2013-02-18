import itertools
import time

t = time.clock()

def tupleToInt(tuple):
	return reduce(lambda rst, d: rst * 10 + d, tuple)

def checkVal(val):
	divisors = [2,3,5,7,11,13,17]
	for i in range(0, 7):
		if tupleToInt(val[i+1:i+4]) % divisors[i] != 0:
			return False

	return True

interestingSum = 0

for val in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
	interestingSum += tupleToInt(val) if checkVal(val) else 0

print interestingSum

print time.clock() - t