import time
start = time.time()

content = open('annexes\\19.txt', 'r').read().split('\n')

changes = {}
existingChanges = []
mollec = content[44]

for line in content :
    if line == '' :
        break
    splits = line.split(' ')
    try :
        changes[splits[0]].append(splits[2])
    except :
        changes[splits[0]] = [splits[2]]
        existingChanges.append(splits[0])

mollecules = {}

for i in range(len(mollec)) :
    if mollec[i] in existingChanges :
        for atome in changes[mollec[i]] :
            newMol = mollec[:i]+atome+mollec[i+1:]
            try :
                if mollecules[newMol] :
                    True
            except :
                mollecules[newMol] = True
    if mollec[i:i+2] in existingChanges :
        for atome in changes[mollec[i:i+2]] :
            newMol = mollec[:i]+atome+mollec[i+2:]
            try :
                if mollecules[newMol] :
                    True
            except :
                mollecules[newMol] = True

resultA = len(mollecules)

changes = {}
existingChanges = []
mollec = content[44]

for line in content :
    if line == '' :
        break
    splits = line.split(' ')
    changes[splits[2]] = splits[0]
    existingChanges.append(splits[2])

dones = {}
mini = 999999999

def decreaseMol(current,nb) :
    global changes
    global existingChanges
    global mini
    global dones

    if mini <= nb :
        return 999999999

    try :
        if dones[current] :
            return 999999999
    except :
        dones[current] = True

    if current == 'e' :
        return -1*nb

    for part in existingChanges :
        id = 0
        while part in current[id:] :
            mini = min(mini, decreaseMol(current[:current.index(part, id)]+changes[part]+current[current.index(part, id)+len(part):], nb+1))
            id = current.index(part, id) +1
            if mini == 0 :
                break
        if mini == 0 :
            break
    return mini

resultB = -1*decreaseMol(mollec, 0)

print('\nAdvent of Code 2015\n19-A :', resultA,'\n19-B :', resultB,'\nIn   :', "%.2f" % (time.time()-start),'sec\n')
