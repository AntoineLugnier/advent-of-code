content = open('annexes\\2015_01_B.txt', 'r').read()

floor = 0
for i in range (0,len(content)):
    if content[i] == '(':
        floor += 1
    elif content[i] == ')':
        floor -= 1
    if floor < 0:
        break

input(i+1)
