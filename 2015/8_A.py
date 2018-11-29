content = open("annexes\\8.txt",'r').read().split('\n')

between = 0

for line in content :
    test = line
    new = ''
    nope = 0
    for i in range(0, len(test)):
        if nope == 0 :
            if test[i] == '"':
                test = test[:i]+'a'+test[i+1:]
            elif test[i] == '\\':
                if test[i+1] == 'x':
                    test = test[:i]+'aaaa'+test[i+4:]
                    nope = 3
                else :
                    test = test[:i]+'aa'+test[i+2:]
                    nope = 1
                new += 'a'
            else :
                new += 'a'
        else :
            nope -= 1
    between += len(test) - len(new)

print('Answer : ' + str(between))
