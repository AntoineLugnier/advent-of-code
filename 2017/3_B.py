def voisins(x, y, dict) :
    sum = 0
    for i in range (-1,2) :
        for j in range (-1,2) :
            if not (i == j == 0) :
                try :
                    sum += dict[(x+i,y+j)]
                except :
                    True
    return sum

input = 265149

dict = {(0,0) : 1}
step = 1

posX = 0
posY = 0

continuer = True
while continuer :
    #right
    for i in range(step) :
        posX += 1
        nb = voisins(posX, posY, dict)
        if nb > input :
            print(nb)
            continuer = False
        else :
            dict[(posX,posY)] = nb
    #up
    for i in range(step) :
        posY += 1
        nb = voisins(posX, posY, dict)
        if nb > input :
            print(nb)
            continuer = False
        else :
            dict[(posX,posY)] = nb
    step += 1

    #left
    for i in range(step) :
        posX -= 1
        nb = voisins(posX, posY, dict)
        if nb > input :
            print(nb)
            continuer = False
        else :
            dict[(posX,posY)] = nb
    #down
    for i in range(step) :
        posY -= 1
        nb = voisins(posX, posY, dict)
        if nb > input :
            print(nb)
            continuer = False
        else :
            dict[(posX,posY)] = nb
    step += 1
