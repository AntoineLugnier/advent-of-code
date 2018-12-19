import time
start = time.time()

content = open("annexes\\9.txt",'r').read().split('\n')

distances = {}
towns = []

for line in content :
    if line != "" :
        elements = line.split(' ')
        if not elements[0] in towns :
            towns.append(elements[0])
        if not elements[2] in towns :
            towns.append(elements[2])
        distances[(elements[0],elements[2])] = int(elements[4])
        distances[(elements[2],elements[0])] = int(elements[4])

def optiWay(town, dists, minMax) :
    global distances

    copyDists = dists.copy()
    copyDists.pop(copyDists.index(town))

    if len(copyDists) == 0 :
        return 0
    if minMax == 'min' :
        return min(distances[(town, nextTown)]+optiWay(nextTown, copyDists, minMax) for nextTown in copyDists)
    else :
        return max(distances[(town, nextTown)]+optiWay(nextTown, copyDists, minMax) for nextTown in copyDists)

print('\nAdvent of Code 2015\n9-A :', min(optiWay(town, towns, 'min') for town in towns),'\n9-B :', max(optiWay(town, towns, 'max') for town in towns),'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
