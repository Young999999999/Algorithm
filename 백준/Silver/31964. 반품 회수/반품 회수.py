n = int(input())
X = list(map(int,input().split()))
T = list(map(int,input().split()))

MAX = 0
for i in range(n):
    MAX = max(MAX,X[i]+T[i])

MAX = max(MAX,2*max(X))

print(MAX)