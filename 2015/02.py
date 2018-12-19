import time
start = time.time()

content = open('annexes\\2.txt', 'r').read().split('\n')

totalA, totalB = 0, 0
for gift in content :
    if gift != '':
        dims = gift.split('x')
        l = int(dims[0])
        L = int(dims[1])
        h = int(dims[2])

        #2-A Total increment
        totalA += (2*(l*L + l*h + L*h)) + min(l*L, l*h, L*h)

        #2-B Total increment
        totalB += (2*(l + h + L)) + l*L*h - 2*max(l,L,h)

print('\nAdvent of Code 2015\n2-A :', totalA,'\n2-B :', totalB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
