t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    step = 1
    xsum = 0
    ysum = 0
    cnt = 0
    bit = 1
    while xsum + ysum < y-x :
        if bit:
            xsum +=step
            bit = 0
        else:
            ysum +=step
            bit = 1
        cnt += 1

        if bit:
            step +=1
    print(cnt)

