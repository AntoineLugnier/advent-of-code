import time
start = time.time()

content = open('annexes\\3.txt', 'r').read()

x, y, x1, x2, y1, y2 = 0, 0, 0, 0, 0, 0
housesA, housesB = 1, 1
visitedA, visitedB = [(0,0)], [(0,0)]

for i in range(0,len(content)):
    if content[i] == '^' :
        y += 1
        if i%2 == 0 :
            y1 += 1
        else :
            y2 += 1
    elif content[i] == 'v' :
        y -= 1
        if i%2 == 0 :
            y1 -= 1
        else :
            y2 -= 1
    elif content[i] == '>' :
        x += 1
        if i%2 == 0 :
            x1 += 1
        else :
            x2 += 1
    elif content[i] == '<' :
        x -= 1
        if i%2 == 0 :
            x1 -= 1
        else :
            x2 -= 1

    #3-A House counting
    if not (x,y) in visitedA:
        housesA += 1
        visitedA.append((x,y))

    #3-B House counting
    if not (x1,y1) in visitedB :
        housesB += 1
        visitedB.append((x1,y1))
    if not (x2,y2) in visitedB :
        housesB += 1
        visitedB.append((x2,y2))

print('\nAdvent of Code 2015\n3-A :', housesA,'\n3-B :', housesB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
