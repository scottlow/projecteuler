import time

t = time.clock()

first = 1
second = 1
sum = 0
count = 2

while True:
	sum = first + second
	first = second
	second = sum

	count += 1

	if(len(str(sum)) == 1000):
		print count
		break

print "Time: ",time.clock()-t