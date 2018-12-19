import time
start = time.time()

array = []

def refreshArray(corners):
    content = open("annexes\\18.txt", 'r').read().split('\n')
    global array
    array = []
    for line in content :
        if line != '' :
            tempArray = list(line)
            array.append(tempArray)
    if corners :
        array[0][0], array[0][len(array)-1], array[len(array)-1][0], array[len(array)-1][len(array)-1] = '#', '#', '#', '#'

def getNeigh (posX,posY) :
    global array
    nbNeigh = 0
    for i in range(-1,2) :
        for j in range(-1,2) :
            if (not (i == j == 0)) and posX+i >= 0 and posY+j >= 0:
                try :
                    if array[posX+i][posY+j] == '#' :
                        nbNeigh += 1
                except :
                    True
    return nbNeigh

def newGen(corners) :
    global array
    newArray = [['.' for i in range(len(array))] for j in range(len(array))]
    for x in range(len(array)) :
        for y in range(len(array)) :
            if array[x][y] == '#' :
                if getNeigh(x,y) == 2 or getNeigh(x,y) == 3 :
                    newArray[x][y] = '#'
            else :
                if getNeigh(x,y) == 3 :
                    newArray[x][y] = '#'
    array = newArray
    if corners :
        array[0][0], array[0][len(array)-1], array[len(array)-1][0], array[len(array)-1][len(array)-1] = '#', '#', '#', '#'


corners, resultA, resultB = False, 0, 0
for i in range(2) :
    refreshArray(corners)
    for i in range(100) :
        newGen(corners)

    lightsOn = 0
    for x in range(len(array)) :
        lightsOn += array[x].count('#')

    if resultA == 0 :
        resultA = lightsOn
    else :
        resultB = lightsOn
    corners = not corners

print('\nAdvent of Code 2015\n18-A :', resultA,'\n18-B :', resultB,'\nIn   :', "%.2f" % (time.time()-start),'sec\n')
