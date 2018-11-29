content = open('annexes\\2.txt', 'r').read().split('\n')

total = 0
for gift in content :
    if gift != '':
        dims = gift.split('x')
        l = int(dims[0])
        L = int(dims[1])
        h = int(dims[2])
        total += (2*(l*L + l*h + L*h)) + min(l*L, l*h, L*h)

print('Answer : ' + str(total))
