import sys
input =sys.stdin.readline
n = int(input())
a,b,c,d,=[0]*n,[0]*n,[0]*n,[0]*n
for i in range(n):
    q,w,e,r = map(int,input().split())
    a[i],b[i],c[i],d[i]=q,w,e,r

ab = [0] * (n*n)
cd = [0] * (n*n)
for i in range(n):
    for j in range(n):
        ab[i*n + j] = a[i]+b[j]

for i in range(n):
    for j in range(n):
        cd[i*n + j] = c[i]+d[j]

ab.sort()
cd.sort()

s,e=0,len(cd)-1
cnt =0
while True:
    if s==len(cd) or e==-1:
        break

    if ab[s] > -cd[e]:
        e-=1
    elif ab[s] < -cd[e]:
        s+=1
    else:
        setA = 0
        setB = 0
        for i in range(s,len(cd)):
            if -cd[e] == ab[i]:
                setA+=1
            else:
                break

        for i in range(e,-1,-1):
            if -ab[s] == cd[i]:
                setB += 1
            else:
                break

        s+=setA
        e-=setB
        cnt += setA*setB

print(cnt)

