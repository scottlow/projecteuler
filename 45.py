import math
import time

t = time.clock()

def isPentagonal(num):
	root = (1 + math.sqrt(1 + 24*num)) / 6
	return root == int(root)

def isHexagonal(num):
	root = (0.5 + math.sqrt(0.25 + 2*num)) / 2
	return root == int(root)

n = 286
Tn = n * (n + 1) / 2

while not isPentagonal(Tn) or not isHexagonal(Tn):
	n += 1
	Tn = n * (n + 1) / 2	

print Tn
print time.clock() - t