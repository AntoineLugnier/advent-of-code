content = open("annexes\\6.txt", 'r').read().split('\n')

lights = [[False for x in range(0,1000)] for y in range(0,1000)]

nb = 0

for line in content :
    if len(line) > 6 :
        spliting = line.split(' ')
        if line[:6] == 'toggle' :
            split1 = spliting[1].split(',')
            split2 = spliting[3].split(',')
            for x in range(int(split1[0]),int(split2[0])+1) :
                for y in range(int(split1[1]),int(split2[1])+1) :
                    lights[x][y] = not lights[x][y]
        elif line[:7] == 'turn on' :
            split1 = spliting[2].split(',')
            split2 = spliting[4].split(',')
            for x in range(int(split1[0]),int(split2[0])+1) :
                for y in range(int(split1[1]),int(split2[1])+1) :
                    lights[x][y] = True
        elif line[:8] == 'turn off' :
            split1 = spliting[2].split(',')
            split2 = spliting[4].split(',')
            for x in range(int(split1[0]),int(split2[0])+1) :
                for y in range(int(split1[1]),int(split2[1])+1) :
                    lights[x][y] = False

for x in range(0,1000) :
    for y in range(0,1000) :
        if lights[x][y] :
            nb += 1

print('Answer : ' + str(nb))
