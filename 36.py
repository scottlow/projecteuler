import time
t = time.clock()
print sum([num for num in range(0, 1000000) if str(num) == str(num)[::-1] and "{0:b}".format(num) == "{0:b}".format(num)[::-1]])
print time.clock() - t