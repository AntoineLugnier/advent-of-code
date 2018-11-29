content = open('annexes\\3.txt', 'r').read()

x1, y1, x2, y2 = 0, 0, 0, 0
houses = 1
visited=[(0,0)]

for i in range(0,len(content)):
    if i%2 == 0 :
        if content[i] == '^' :
            y1 += 1
        elif content[i] == 'v' :
            y1 -= 1
        elif content[i] == '>' :
            x1 += 1
        elif content[i] == '<' :
            x1 -= 1

        if not (x1,y1) in visited:
            houses += 1
            visited.append((x1,y1))
    else :
        if content[i] == '^' :
            y2 += 1
        elif content[i] == 'v' :
            y2 -= 1
        elif content[i] == '>' :
            x2 += 1
        elif content[i] == '<' :
            x2 -= 1

        if not (x2,y2) in visited:
            houses += 1
            visited.append((x2,y2))

print('Answer : ' + str(houses))
