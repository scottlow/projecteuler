import time
t = time.clock()

maxSum = 0

for a in range(100):
	for b in range(100):
		num = a**b
		if sum(map(int,str(num))) > maxSum:
			maxSum = sum(map(int,str(num)))

print maxSum
print time.clock() - t