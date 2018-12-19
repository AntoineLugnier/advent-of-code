import time
start = time.time()

content = open('annexes\\5.txt', 'r').read().split('\n')

banlist = ['ab', 'cd', 'pq', 'xy']

countA, countB = 0, 0
for word in content :
    nbVoy = 0
    double, banSub, between, repeat = False, False, False, False

    for i in range(0, len(word)):

        #5-A Tests
        if i != len(word)-1 :
            if word[i:i+2] in banlist :
                banSub = True
            if word[i] == word[i+1] :
                double = True
        if word[i] in ['a','e','i','o','u'] :
            nbVoy += 1

        #5-B Tests
        if i < len(word)-2 :
            if word[i:i+2] in word[:i] or word[i:i+2] in word[i+2:]:
                repeat = True
            if word[i] == word[i+2] :
                between = True

    #5-A Conditions check
    if (not banSub) and double and (nbVoy >= 3) :
        countA += 1

    #5-B Conditions check
    if repeat and between :
        countB += 1


print('\nAdvent of Code 2015\n5-A :', countA,'\n5-B :', countB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
