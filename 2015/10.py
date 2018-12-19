import time
start = time.time()

input = '1113122113'
test = [('a', '111', '31'), ('b', '11','21'), ('c', '1','11'), ('d', '222','32'), ('e', '22','22'), ('f', '2', '12'), ('g', '333', '33'), ('h', '33', '23'), ('i', '3', '13')]

resA, resB = '', ''

def next(stri):
    newStr = stri
    n = 1
    digit = stri[0]
    for i in range (1,len(stri)) :
        if stri[i] == digit :
            n += 1
        else :
            newStr += str(n) + digit
            digit = stri[i]
            n = 1
    newStr += str(n) + digit
    return newStr

def next2(stri):
    global test
    for k in test :
        stri = stri.replace(k[1], k[0])
    for k in test :
        stri = stri.replace(k[0], k[2])
    return stri

for i in range(1, 51) :
    input = next2(input)
    if i == 40 :
        resA = len(input)
    if i == 50 :
        resB = len(input)

print('\nAdvent of Code 2015\n10-A :', resA,'\n10-B :', resB,'\nIn   :', "%.2f" % (time.time()-start),'sec\n')
