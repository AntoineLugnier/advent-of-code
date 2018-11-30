content = open('annexes\\4.txt', 'r').read().split('\n')

valids = 0
for line in content :
    if line != '' :
        words = line.split(' ')
        valid = True
        for i in range(len(words)-1) :
            for j in range (i+1, len(words)) :
                if sorted(words[i]) == sorted(words[j]) :
                    valid = False
        if valid :
            valids += 1

print(valids)
 
