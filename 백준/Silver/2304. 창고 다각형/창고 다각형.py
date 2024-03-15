import sys
input = sys.stdin.readline

# 레이저 쏴서 2개면 False
# 레이저 쏴서 1개면 True -> abs(idx - i) * height
# 레이저 솨서 0개면 True -> 1 * height


def judge(idx):
    Lraser = 0
    Rraser = 0

    for ridx in range(idx+1,1001):
        if pole[idx] <= pole[ridx]:
            Rraser += 1
            break


    for lidx in range(idx-1,-1,-1):
        if pole[idx] < pole[lidx]:
            Lraser += 1
            break


    if Lraser == 1 and Rraser == 1:
        return

    elif Lraser == 1 :
        sum[0] += (idx - lidx) * pole[idx]
    elif Rraser == 1 :
        sum[0] += (ridx - idx ) * pole[idx]
    else:
        sum[0] += pole[idx]

    return


N = int(input())
pole = [0 for i in range(1001)]
sum = [0]
start=[]

for i in range(N):
    L,H = map(int,input().split())
    pole[L] = H
    start.append((L,H))


start.sort()
for i in range(N):
    judge(start[i][0])

print(sum[0])


