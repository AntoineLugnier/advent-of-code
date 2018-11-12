content = open('annexes\\2015_05_A.txt', 'r').read().split('\n')

banlist = ['ab', 'cd', 'pq', 'xy']

count = 0
for word in content :
    between = False
    double = False
    for i in range(0, len(word)):
        if i < len(word)-2 :
            if word[i:i+2] in word[:i] or word[i:i+2] in word[i+2:]:
                double = True
            if word[i] == word[i+2] :
                between = True
    if double and between :
        count += 1

input(count)
