# Never run this code.

base = "0123456789"

count = 0

def toString(intBase):
	stringBase = str(intBase)
	if len(stringBase) != 10:
		return "0" + stringBase

def containsAllDigits(base):
	booleanArray = [False] * 10

	for c in base:
		if booleanArray[int(c) - 1] == False:
			booleanArray[int(c) - 1] = True
		else:
			return False
	return True

while count != 1000000:
	while True:
		intBase = int(base)
		intBase += 1
		base = toString(intBase)
		if(containsAllDigits(base)):
			break
	count += 1

print base