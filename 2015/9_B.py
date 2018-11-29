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

def shortestWay(town, dists) :
    global distances

    copyDists = dists.copy()
    copyDists.pop(copyDists.index(town))

    if len(copyDists) == 0 :
        return 0
    return max(distances[(town, nextTown)]+shortestWay(nextTown, copyDists) for nextTown in copyDists)

print(max(shortestWay(town, towns) for town in towns))
