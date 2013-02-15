def isLeapYear(year):
	return year % 4 == 0 and year % 100 == 0 and year % 400 != 0

year = 1901
day = 6 # first Sunday in 1901
i = 0
sundayCount = 0

while year != 2001:
	months = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	
	months.insert(1, 29 if isLeapYear(year) else 28)

	while i < len(months):
		if(day + 7 > months[i]):
			day = (day + 7) % months[i];
			i += 1
		else: day += 7
		if(day == 1):
			sundayCount += 1

	i = 0
	year += 1

print sundayCount