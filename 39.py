import time
import fractions

t = time.clock()

solutionMatrix = [0] * 1001

for m in range(1, 22):
	for n in range (1, m):
		if(m > n and (m - n) % 2 == 1 and fractions.gcd(m, n) == 1):
			p = 2 * m * m + 2 * m * n
			if (p > 1000):
				break

			for i in range(p, 1001, p):
				solutionMatrix[i] += 1

print solutionMatrix.index(max(solutionMatrix))
print(time.clock() - t)

