import hashlib

n = 1
while True :
    m = hashlib.md5()
    m.update(b"bgvyzdsv%d" % n)
    if m.hexdigest()[0:6]=='000000' :
        print('Answer : ' + str(n))
        break
    n+=1
