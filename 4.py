first = 999
second = 999

palindromes = []
large = 0

def isPalindrome(n):

	string = str(n)

	i = 0
	j = len(string) - 1

	while i < j:
		if string[i] != string[j]:
			return False

		i += 1
		j -= 1

	return True

while first != 0:
	second = 999
	while second != 0:
		product = first * second

		if isPalindrome(product):
			palindromes.append(product)

		second -= 1
	first -= 1

for s in palindromes:
	if s > large:
		large = s

print large