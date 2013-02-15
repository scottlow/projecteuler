import time

t = time.clock()

sum = 0
i = 1
sideLen = 3

while sideLen <= 1001:
	while i <= sideLen ** 2:
		sum += i
		i += sideLen - 1 if i != sideLen ** 2 else sideLen + 1
	sideLen += 2

print sum

print (time.clock() - t)

