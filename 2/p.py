first = 1
second = 1

sum = 0
result = 0

while True:

	if(sum > 4000000):
		break

	sum = first + second
	first = second
	second = sum

	if(sum % 2 == 0):
		result += sum

print result