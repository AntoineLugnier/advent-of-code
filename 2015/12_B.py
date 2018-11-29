content = open('annexes\\12.txt', 'r').read()

def deleteDicts(stri, value) :
    if value in stri :
        splits = stri.split(value,1)
        indStart, indexEnd = 0, 0
        rank = 1
        for i in range(len(splits[0])-1, -1, -1) :
            if splits[0][i] == '{' or splits[0][i] == '[':
                rank -= 1
            if splits[0][i] == '}' or splits[0][i] == ']':
                rank += 1
            if rank == 0 :
                if splits[0][i] == '{' :
                    indStart = i
                else :
                    indStart = len(splits[0])
                break
        rank = 1
        for i in range (len(splits[1])) :
            if splits[1][i] == '{' or splits[1][i] == '[':
                rank += 1
            if splits[1][i] == '}' or splits[1][i] == ']':
                rank -= 1
            if rank == 0 :
                if splits[1][i] == '}' :
                    indexEnd = i+1
                else :
                    indexEnd = 0
                break
        return deleteDicts(splits[0][:indStart]+splits[1][indexEnd:], value)
    else :
        return stri

content = deleteDicts(content, '"red"')

total = 0
i=0
nb = ''
while i < len(content) :
    if content[i] in ['-','0','1','2','3','4','5','6','7','8','9'] :
        nb += content[i]
    else :
        if nb != '' :
            total += int(nb)
            nb = ''
    i += 1
if nb != '' :
    total += int(nb)
print(total)
