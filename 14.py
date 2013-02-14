i = 1
maxSeq = 0
maxNum = 0;

def sequence(n):

	length = 0
	while n > 1:
		if n & 1 == 0:
			n /= 2
		else:
			n = 3*n + 1
		length += 1 
	return length

while i < 999999:
	test = sequence(i)
	if test > maxSeq:
		maxSeq = test
		maxNum = i
	i += 1

print maxNum

