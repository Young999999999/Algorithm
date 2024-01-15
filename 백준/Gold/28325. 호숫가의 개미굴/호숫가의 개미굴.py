import sys
input= sys.stdin.readline

def judge(x):

    if not visited[x-1]  and  not visited[(x+1)%n] :
        visited[x] = True






n = int(input())
c =list(map(int,input().split()))
visited=[False]*(n)


result = sum(c)


for i in range(n):
    if c[i] == 0 :
        judge(i)


print(result+visited.count(True))
