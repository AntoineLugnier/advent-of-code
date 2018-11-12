content = open('annexes\\5_A.txt', 'r').read().split('\n')

cases = []
for element in content :
    if element != '' :
        cases.append(int(element))

pos = 0
steps = 0
while pos < len(cases) and pos >= 0 :
    steps += 1
    tempP = pos
    pos += cases[pos]
    cases[tempP] += 1

input(steps)
