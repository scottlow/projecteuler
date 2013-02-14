num = [3, 3, 5, 4, 4, 3, 5, 5, 4] # 1 - 9
num1 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 10 - 19
num2 = [6, 6, 5, 5, 5, 7, 6, 6] # 20, 30, 40, etc.

hundred = 7
oneHundredAnd = 10

oneToNineteen = sum(num) + sum(num1)
twentyToNinetyNine = sum(num2)

theRest = 0

for i in range(1, len(num)):
	twentyToNinetyNine += (num1[i] * len(num) + sum(num))

for i in range(1, len(num)):
	theRest += hundred * num[i]

theRestButNot = oneToNineteen + twentyToNinetyNine

for i in range(1, len(num)):
	theRest += theRestButNot + 99 * oneHundredAnd

print oneToNineteen + twentyToNinetyNine + theRest
