content = open('annexes\\3.txt', 'r').read()

x = 0
y = 0
houses = 1
visited=[(0,0)]

for i in range(0,len(content)):
    if content[i] == '^' :
        y += 1
    elif content[i] == 'v' :
        y -= 1
    elif content[i] == '>' :
        x += 1
    elif content[i] == '<' :
        x -= 1

    if not (x,y) in visited:
        houses += 1
        visited.append((x,y))

print('Answer : ' + str(houses))
