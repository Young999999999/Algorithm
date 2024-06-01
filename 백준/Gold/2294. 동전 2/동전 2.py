import sys
from collections import deque


input = sys.stdin.readline

def BFS():
    q = deque()
    for i in vector:
        q.append(i)

    while q:
        num = q.popleft()
        for i in vector:
            if num+i > k:
                continue

            if dp[num+i] == 0:
                dp[num+i] = dp[num] + 1
                q.append(num+i)

            if num+i == k:
                print(dp[k])
                exit(0)

n,k = map(int,input().split())

vector = []
dp = [0] * (100001)

for i in range(n):
    vector.append(int(input()))

for i in vector:
    dp[i]=1

BFS()
print(-1)

