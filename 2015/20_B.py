import math
import functools
import time

input = 33100000
start = time.time()

@functools.lru_cache(maxsize=None)
def getHouseSum(nb) :
    divs = [nb]
    for i in range(2,int(math.ceil(math.sqrt(nb)))) :
        if nb%i == 0 :
            divs.append(int(nb/i))
    return sum(x if x*50>=nb else 0 for x in divs)*11

n = 1000
while True :
    if input <= getHouseSum(n) :
        print(n)
        break
    if n % 10000 == 0 :
        print(n)
    n+=1

print((time.time()-start)/1000)
