import time
start = time.time()

content = open('annexes\\1.txt', 'r').read()

floor, idB = 0, -1
for i in range (0,len(content)):

    #1-A Count
    if content[i] == '(':
        floor += 1
    elif content[i] == ')':
        floor -= 1

    #1-B Test
    if floor < 0 and idB < 0:
        idB = i+1

print('\nAdvent of Code 2015\n1-A :', floor,'\n1-B :', idB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
