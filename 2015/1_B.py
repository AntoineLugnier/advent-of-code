content = open('annexes\\1_B.txt', 'r').read()

floor = 0
for i in range (0,len(content)):
    if content[i] == '(':
        floor += 1
    elif content[i] == ')':
        floor -= 1
    if floor < 0:
        break

print('Answer : ' + str(i+1))
