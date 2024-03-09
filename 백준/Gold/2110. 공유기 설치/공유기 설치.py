import sys
input = sys.stdin.readline
N,C = map(int,input().split())
l = []
for i in range(N):
    l.append(int(input()))
l.sort()
dist = []
pre=-1
for i in l:
    if pre == -1:
        pre = i
        continue

    dist.append(i-pre)
    pre=i

s=1
e=1000000001

def judge(line):
    cur = 0
    cnt = 0
    for i in dist:
        cur += i
        if cur >= line:
            cnt +=1
            cur = 0

    if cnt >= C-1:
        return True
    return False


for i in range(32):
    mid=(s+e)//2

    if judge(mid):
        s=mid
    else:
        e=mid

print(s)