<<<<<<< HEAD
oneToNine = [3, 3, 5, 4, 4, 3, 5, 5, 4] # 1 - 9
tenToNineteen = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 10 - 19
twentyToNinety = [6, 6, 5, 5, 5, 7, 6, 6] # 20, 30, 40,..., 90

hundred = 7
hundredAnd = 10
oneThousand = 11

oneHundredTo999 = 0

#1, 2, ... , 19
oneToNineteen = sum(oneToNine) + sum(tenToNineteen)

# 20, 30, 40, ..., 90
twentyToNinetyNine = sum(twentyToNinety)

# 20, 21, ... 99
for i in range(0, len(twentyToNinety)):
	twentyToNinetyNine += ((twentyToNinety[i] * 9) + sum(oneToNine))

oneToNinetyNine = oneToNineteen + twentyToNinetyNine

#100, 200, ... , 900
for i in range(0, len(oneToNine)):
	oneHundredTo999 += oneToNine[i] + hundred

#101, 102,..., 999
for i in range(0, len(oneToNine)):
	oneHundredTo999 += (oneToNine[i] + hundredAnd) * 99 + oneToNinetyNine

print oneToNinetyNine + oneHundredTo999 + oneThousand
