content = open('annexes\\1.txt', 'r').read().replace('\n','')

match = 0

for i in range (len(content)) :
    if i == len(content)-1 :
        if content[i] == content[0] :
            match += int(content[i])
    else :
        if content[i] == content[i+1] :
            match += int(content[i])
print(match)
