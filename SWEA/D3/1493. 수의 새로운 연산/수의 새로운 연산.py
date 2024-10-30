t = int(input())

def findPos(value):
    pre = 0
    for line in range(10000):
        pre += line
        if pre >= value :
            break

    pre -= line-1
    x = 1
    y = line

    while pre != value :
        pre += 1
        x += 1
        y -= 1

    return x,y

for i in range(t):
    p,q = map(int,input().split())
    px,py = findPos(p)
    qx,qy = findPos(q)

    x = px + qx
    y = py + qy

    result = 0
    for j in range(x+1):
        result += j

    for j in range(y-1):
        result += j + x

    print("#{} {}".format(i+1,result))