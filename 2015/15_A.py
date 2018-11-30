content = open("annexes\\15.txt",'r').read().split('\n')

ingredients = []

for line in content :
    if line != '' :
        stats = line.split(' ')
        ingredients.append([int(stats[2][:len(stats[2])-1]), int(stats[4][:len(stats[4])-1]), int(stats[6][:len(stats[6])-1]), int(stats[8][:len(stats[8])-1]), int(stats[10])])

maxi = 0
for a in range(1,98) :
    for b in range(1,99-a) :
        for c in range (1,100 - a - b) :
            d = 100 - a - b - c
            capacity = ingredients[0][0]*a + ingredients[1][0]*b + ingredients[2][0]*c +ingredients[3][0]*d
            if capacity < 0 :
                capacity = 0
            durability = ingredients[0][1]*a + ingredients[1][1]*b + ingredients[2][1]*c +ingredients[3][1]*d
            if durability < 0 :
                durability = 0
            flavor = ingredients[0][2]*a + ingredients[1][2]*b + ingredients[2][2]*c +ingredients[3][2]*d
            if flavor < 0 :
                flavor = 0
            texture = ingredients[0][3]*a + ingredients[1][3]*b + ingredients[2][3]*c +ingredients[3][3]*d
            if texture < 0 :
                texture = 0
            if texture * durability * flavor * capacity > maxi :
                maxi = texture * durability * flavor * capacity

print(maxi)
