import time
import math
t = time.clock()

digits = math.factorial(100)

print sum(int(digit) for digit in str(digits))
print time.clock() - t