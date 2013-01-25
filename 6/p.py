import math

def calculateSquareSum(n):
	return (n * (n+1) * (2 * n+1)) / 6

def calculateSum(n):
	return ((n+1)*n)/2

n = calculateSum(100)

print (n*n) - calculateSquareSum(100)