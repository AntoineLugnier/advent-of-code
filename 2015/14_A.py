content = open('annexes\\14.txt', 'r').read().split('\n')

reineers = {}

for line in content :
    if line != '' :
        splits = line.split(' ')
        reineers[splits[0]] = { 'flySpeed' : int(splits[3]), 'flyTime' : int(splits[6]), 'restTime' : int(splits[13]), 'currentState' : 'flying', 'currentStep' : int(splits[6]), 'totalDist' : 0}

for i in range (2503) :
    for key, value in reineers.items():
        if value['currentState'] == 'flying' :
            value['totalDist'] += value['flySpeed']
        value['currentStep'] -= 1
        if value['currentStep'] == 0 :
            if value['currentState'] == 'flying' :
                value['currentState'] = 'resting'
                value['currentStep'] = value['restTime']
            else :
                value['currentState'] = 'flying'
                value['currentStep'] = value['flyTime']

print(max(value['totalDist'] for key, value in reineers.items()))
