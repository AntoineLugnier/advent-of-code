import time
start = time.time()

content = open("annexes\\7.txt",'r').read().split('\n')

if '' in content :
    content.pop(content.index(''))

tempA, resultA, resultB = -1, '', ''
for i in range(0,2) :
    done = [False for x in range(0,len(content))]
    dict = {}
    while False in done :
        for x in range(0,len(content)) :
            if not done[x] :
                datas = content[x].split(' -> ')
                instruction = datas[0].split(' ')
                try :
                    if len(instruction) == 1 :
                        if datas[1] == 'b' and tempA >= 0:
                            dict['b'] = tempA
                        else :
                            try :
                                dict[datas[1]] = int(instruction[0])
                            except :
                                dict[datas[1]] = dict[instruction[0]]
                    elif len(instruction) == 2 :
                        dict[datas[1]] = ~dict[instruction[1]]
                    else :
                        try :
                            nbT1 = int(instruction[0])
                        except :
                            nbT1 = dict[instruction[0]]
                        try :
                            nbT2 = int(instruction[2])
                        except :
                            nbT2 = dict[instruction[2]]
                        if instruction[1] == 'AND' :
                            dict[datas[1]] = nbT1 & nbT2
                        elif instruction[1] == 'OR' :
                            dict[datas[1]] = nbT1 | nbT2
                        elif instruction[1] == 'LSHIFT' :
                            dict[datas[1]] = nbT1 << nbT2
                        elif instruction[1] == 'RSHIFT' :
                            dict[datas[1]] = nbT1 >> nbT2
                    done[x] = True
                except :
                    True
    tempA = dict['a']
    if resultA == '' :
        resultA = dict['a']
    else :
        resultB = dict['a']

print('\nAdvent of Code 2015\n7-A :', resultA,'\n7-B :', resultB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
