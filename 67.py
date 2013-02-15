f = open('resources/p67.txt', 'r')

numLines = [[int(x) for x in line.split(" ")] for line in f]

i = len(numLines) - 1
sum = 0

while i > 0:
	currentLine = numLines[i]
	nextLine = numLines[i-1]
	j = 1
	while j < len(currentLine):
		maximum = max(currentLine[(j - 1): j + 1])
		nextLine[j - 1] += maximum
		j += 1
	i -= 1

print numLines[0][0]