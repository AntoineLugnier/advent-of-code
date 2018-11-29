content = open('annexes\\4.txt', 'r').read().split('\n')

valids = 0
for line in content :
    if line != '' :
        words = line.split(' ')
        for i in range(len(words)-1) :
            if words[i] in words[i+1:] :
                break
        else :
            valids += 1

print(valids)
