import time
start = time.time()

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

resultA = between

between = 0

for line in content :
    if line != '' :
        test = line
        new = 2
        nope = 0
        for i in range(0, len(test)):
            if test[i] == '"' or test[i] == '\\':
                new += 2
            else :
                new += 1
        between += new - len(test)

resultB = between

print('\nAdvent of Code 2015\n8-A :', resultA,'\n8-B :', resultB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
