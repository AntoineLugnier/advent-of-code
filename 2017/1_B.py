content = open('annexes\\1.txt', 'r').read().replace('\n','')

match = 0

step = int(len(content)/2)

for i in range (step) :
    if content[i] == content[i+step] :
        match += int(content[i])*2
print(match)
