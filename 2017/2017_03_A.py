def test(i):
    return [(i*2+1)*(i*2+1) , (i*2)*(i*2)-(i*2-1) , (i*2)*(i*2)+1 , (i*2)*(i*2)+(i*2)+1]

t = 265149

maxi = 1
rank = 0

run = True

while run :
    rank += 1
    v = sorted(test(rank))

    if t < min(v.copy()) :
        mid = (v[1]-v[0])/2
        print(rank + abs(v[0]-mid-t))
        run = False

    if min(v) <= t and max(v) >= t :
        mid = (v[1]-v[0])/2
        for i in range(0,3):
            if v[i]<= t and v[i+1]>=t :
                print(rank + abs(v[i]+mid-t))
                break
        run = False
