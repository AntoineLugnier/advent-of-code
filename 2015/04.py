import hashlib
import time
start = time.time()

answerA, answerB = 0, 0
n = 1

#4-A Loop
while True :
    m = hashlib.md5()
    m.update(b"bgvyzdsv%d" % n)
    if m.hexdigest()[0:5]=='00000' :
        answerA = n
        break
    n+=1

#4-B Loop
while True :
    m = hashlib.md5()
    m.update(b"bgvyzdsv%d" % n)
    if m.hexdigest()[0:6]=='000000' :
        answerB = n
        break
    n+=1

print('\nAdvent of Code 2015\n4-A :', answerA,'\n4-B :', answerB,'\nIn  :', "%.2f" % (time.time()-start),'sec\n')
