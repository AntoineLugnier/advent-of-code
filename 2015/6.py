import time
start = time.time()

content = open("annexes\\6.txt", 'r').read().split('\n')

lightsA = [[False for x in range(0,1000)] for y in range(0,1000)]
lightsB = [[0 for x in range(0,1000)] for y in range(0,1000)]

nbA, nbB = 0, 0

for line in content :
    if len(line) > 6 :
        spliting = line.split(' ')
        if line[:6] == 'toggle' :
            split1 = spliting[1].split(',')
            split2 = spliting[3].split(',')
            for x in range(int(split1[0]),int(split2[0])+1) :
                for y in range(int(split1[1]),int(split2[1])+1) :
                    lightsA[x][y] = not lightsA[x][y]
                    lightsB[x][y] += 2
        elif line[:7] == 'turn on' :
            split1 = spliting[2].split(',')
            split2 = spliting[4].split(',')
            for x in range(int(split1[0]),int(split2[0])+1) :
                for y in range(int(split1[1]),int(split2[1])+1) :
                    lightsA[x][y] = True
                    lightsB[x][y] += 1
        elif line[:8] == 'turn off' :
            split1 = spliting[2].split(',')
            split2 = spliting[4].split(',')
            for x in range(int(split1[0]),int(split2[0])+1) :
                for y in range(int(split1[1]),int(split2[1])+1) :
                    lightsA[x][y] = False
                    if lightsB[x][y] != 0 :
                        lightsB[x][y] -= 1

for x in range(0,1000) :
    for y in range(0,1000) :
        if lightsA[x][y] :
            nbA += 1
        nbB += lightsB[x][y]

print('\nAdvent of Code 2015\n6-A :', nbA,'\n6-B :', nbB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
