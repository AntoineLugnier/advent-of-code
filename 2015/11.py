import time
start = time.time()

password = 'hxbxwxba'

def increase(pwd) :
    if pwd[-1] == 'z' :
        return increase(pwd[:len(pwd)-1])+'a'
    else :
        return pwd[:len(pwd)-1]+chr(ord(pwd[-1])+1)

goodPwd = False
passwordA, passwordB = '', ''

while not goodPwd :
    password = increase(password)
    pairs = []
    incrStr = False

    for i in range(len(password)-1) :
        if i < len(password)-2 :
            if ord(password[i])+2 == ord(password[i+1])+1 == ord(password[i+2]) :
                incrStr = True
        if ord(password[i]) == ord(password[i+1]) :
            if not password[i:i+2] in pairs :
                pairs.append(password[i:i+2])
        if len(pairs) >= 2 and incrStr and not 'i' in password and not 'o' in password and not 'l' in password :
            if passwordA == '' :
                passwordA = password
            else :
                passwordB = password
                goodPwd = True
                break

print('\nAdvent of Code 2015\n11-A :', passwordA,'\n11-B :', passwordB,'\nIn   :', "%.2f" % (time.time()-start),'sec\n')
