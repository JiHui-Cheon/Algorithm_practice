import time
import random
from os import listdir

print(time.time())
print(time.ctime())

print(type(time.ctime()))

cur_time = time.ctime()
print(cur_time.split(' ')[-1])

for i in range(5):
    print(i)
    time.sleep(1)

print(time)
print(random)
print(dir(time))

print(dir())

