from collections import deque

n = int(input())

prime = [-1] * 10000

for i in range(2,10000):
    if prime[i] == -1:
        prime[i] = 1
        for j in range(i+i,10000,i):
            prime[j] = 0

def getTransitionCandidate(num):

    tmp = []
    target = num
    num = [num//1000,num%1000//100,num%100//10,num%10]
    origin = num[:]

    for i in range(4):
        num = origin[:]
        for j in range(10):
            num[i] = j

            if i == 0 and j==0:
                continue

            result = int("".join(map(str, num)))

            if result == target:
                continue
            tmp.append(result)

    return tmp

for i in range(n):
    a,b = list(map(int,input().split()))
    q = deque()
    q.append((a,0))
    visited = [False] * 10000
    visited[a] = True
    flag = 0
    while q:
        now, cnt = q.popleft()

        if now == b:
            flag = 1
            print(cnt)
            break

        for next in getTransitionCandidate(now):
            if not prime[next]:
                continue

            if not visited[next]:
                visited[next] = True
                q.append((next,cnt+1))


    if not flag:
        print("Impossible")