content = open('annexes\\2015_01_A.txt', 'r').read()

floor = 0
for i in range (0,len(content)):
    if content[i] == '(':
        floor += 1
    elif content[i] == ')':
        floor -= 1

input(floor)
