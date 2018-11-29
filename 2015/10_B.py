start = '1113122113'

def next(stri):
    newStr = ''
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

for i in range(0, 50) :
    start = next(start)

print(len(start))
