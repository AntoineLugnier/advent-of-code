import time
start = time.time()

containers = []

for line in open('annexes\\17.txt', 'r').read().split('\n') :
    if line != '':
        containers.append(int(line))

def nbCombinationsA (liste, total) :
    if total == 150 :
        return 1
    elif total > 150 or len(liste) == 0:
        return 0
    else :
        return sum(nbCombinationsA(liste[i+1:],total+liste[i]) for i in range(len(liste)))

def nbCombinationsB (liste, total, nb) :
    if total == 150 :
        return [nb]
    elif total > 150 or len(liste) == 0:
        return [25]
    else :
        arr = []
        for i in range(len(liste)) :
            arr += nbCombinationsB(liste[i+1:], total+liste[i], nb+1)
        return arr

resultA = nbCombinationsA (containers, 0)

array = sorted(nbCombinationsB (containers, 0, 0))
resultB = 0
nbr = array[0]
for i in array :
    if i == nbr :
        resultB += 1
    else :
        break

print('\nAdvent of Code 2015\n17-A :', resultA,'\n17-B :', resultB,'\nIn   :', "%.2f" % (time.time()-start),'sec\n')
