N,M,b = map(int,input().split())
block = []

min_t = 1000000000000000
max_h = -10
for i in range(N):
    block.append(list(map(int,input().split())))

for height in range(0,257):
    get = 0
    used = 0

    for i in range(N):
        for j in range(M):
            if height < block[i][j]:
                get += block[i][j] - height
            else:
                used += height - block[i][j]


    if get+b >= used:
        t= 2*get + used
        if min_t >= t :
            min_t = t
            max_h = height



print(min_t,max_h)