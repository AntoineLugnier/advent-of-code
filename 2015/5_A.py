content = open('annexes\\2015_05_A.txt', 'r').read().split('\n')

banlist = ['ab', 'cd', 'pq', 'xy']

count = 0
for word in content :
    nbVoy = 0
    double = False
    banSub = False
    for i in range(0, len(word)):
        if i != len(word)-1 :
            if word[i:i+2] in banlist :
                banSub = True
            if word[i] == word[i+1] :
                double = True
        if word[i] in ['a','e','i','o','u'] :
            nbVoy += 1
    if (not banSub) and double and (nbVoy >= 3) :
        count += 1

input(count)
