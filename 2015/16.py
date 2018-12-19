import time
start = time.time()

content = open('annexes\\16.txt', 'r').read().split('\n')

tickerTape = {'children' : 3, 'cats' : 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for line in content :
    if line != '' :
        tempVals = {'children' : -1, 'cats' : -1, 'samoyeds': -1, 'pomeranians': -1, 'akitas': -1, 'vizslas': -1, 'goldfish': -1, 'trees': -1, 'cars': -1, 'perfumes': -1}
        splits = line.split(' ')
        tempVals[splits[2][:-1]] = int(splits[3][:-1])
        tempVals[splits[4][:-1]] = int(splits[5][:-1])
        tempVals[splits[6][:-1]] = int(splits[7])

        #16-A Check
        for key, value in tickerTape.items() :
            if tempVals[key] >= 0 :
                if tempVals[key] != value :
                    break
        else :
            resultA = splits[1][:-1]

        #16-B Check
        for key, value in tickerTape.items() :
            if tempVals[key] >= 0 :
                if key == 'cats' or key == 'trees' :
                    if tempVals[key] <= value :
                        break
                elif key == 'pomeranians' or key == 'goldfish' :
                    if tempVals[key] >= value :
                        break
                else :
                    if tempVals[key] != value :
                        break
        else :
            resultB = splits[1][:-1]

print('\nAdvent of Code 2015\n16-A :', resultA,'\n16-B :', resultB,'\nIn   :', "%.2f" % (time.time()-start),'sec\n')
