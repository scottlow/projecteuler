import time
import math

t = time.clock()

def findValue(word):
	return sum(ord(char) - 96 for char in word.lower()[1:-1])

def isTriangleWord(word):
	value = findValue(word)

	# A word is triangular only if (8n + 1) is a perfect square (where n = value of the word)
	# This was calculated via the quadratic formula
	if(math.sqrt(8*value + 1).is_integer()):
		return True
	else:
		return False

f = open("resources/p42.txt", "r")
triangleCount = 0

for word in f.readline().split(','):
	if isTriangleWord(word):
		triangleCount += 1;

print triangleCount

print time.clock() - t