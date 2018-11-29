content = open("annexes\\8.txt",'r').read().split('\n')
if '' in content :
    content.pop(content.index(''))

between = 0

for line in content :
    test = line
    new = 2
    nope = 0
    for i in range(0, len(test)):
        if test[i] == '"' or test[i] == '\\':
            new += 2
        else :
            new += 1
    between += new - len(test)

print('Answer : ' + str(between))
