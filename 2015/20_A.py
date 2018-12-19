import math
import functools
import time

input = 3310000
start = time.time()

@functools.lru_cache(maxsize=None)
def getHouseSum(nb) :
    summ = 1+nb
    for i in range(2,int(math.ceil(math.sqrt(nb)))) :
        if nb%i == 0 :
            summ += i + int(nb/i)
    if math.sqrt(nb)%1 == 0 :
        summ += math.sqrt(nb)
    return summ

n = input/5
while True :
    if input <= getHouseSum(n) :
        print(n)
        break
    if n % 10000 == 0 :
        print(n)
    n+=1

print((time.time()-start))
