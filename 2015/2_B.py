content = open('annexes\\2015_02_A.txt', 'r').read().split('\n')

total = 0
for gift in content :
    if gift != '':
        dims = gift.split('x')
        l = int(dims[0])
        L = int(dims[1])
        h = int(dims[2])
        total += (2*(l + h + L)) + l*L*h - 2*max(l,L,h)

input(total)