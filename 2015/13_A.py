content = open('annexes\\13.txt', 'r').read().split('\n')

sittingNext = {}
peoples = []

for line in content :
    if line != '' :
        splits = line.split(' ')
        if not splits[0] in peoples :
            peoples.append(splits[0])
        if splits[2] == 'gain' :
            sittingNext[(splits[0],splits[10][:len(splits[10])-1])] = int(splits[3])
        else :
            sittingNext[(splits[0],splits[10][:len(splits[10])-1])] = int('-'+splits[3])

def getHappiness(liste):
    global sittingNext
    happiness = 0
    for i in range(len(liste)) :
        happiness += sittingNext[(liste[i],liste[i-1])] + sittingNext[(liste[i],liste[(i+1)%len(liste)])]
    return happiness

def maxHappiness(liste, peoplesL) :
    if peoplesL == [] :
        return getHappiness(liste)
    else :
        return max(maxHappiness(liste+[peoplesL[i]], peoplesL[:i]+peoplesL[i+1:]) for i in range(len(peoplesL)))

print( maxHappiness([], peoples) )
