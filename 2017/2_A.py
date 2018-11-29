content = open('annexes\\2.txt', 'r').read().split('\n')

sum = 0

for line in content :
    if line != '' :
        nbs = line.split('\t')
        for i in range (len(nbs)) :
            nbs[i] = int(nbs[i])
        sum += max(nbs) - min(nbs)

print(sum)
