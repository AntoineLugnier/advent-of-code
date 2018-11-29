content = open('annexes\\12.txt', 'r').read()

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
