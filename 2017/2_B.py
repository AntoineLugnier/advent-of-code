content = open('annexes\\2.txt', 'r').read().split('\n')

sum = 0

for line in content :
    if line != '' :
        nbs = line.split('\t')
        for i in range (len(nbs)) :
            nbs[i] = int(nbs[i])
        for i in range (len(nbs)) :
            for j in range(len(nbs)) :
                if i != j :
                    if nbs[i]/nbs[j] == int(nbs[i]/nbs[j]) :
                        sum += nbs[i]/nbs[j]

print(sum)
