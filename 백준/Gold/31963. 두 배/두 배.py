import sys

input= sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
dp = [0] * n

for i in range(1,n):
    if l[i] >= l[i-1] :
        for j in range(1,21):
            if 2**j * l[i-1] > l[i]:
                dp[i] = max(dp[i-1] - (j-1),0)
                break

    else:
        for j in range(1,21):
            if (2**j) * (l[i]) >= l[i-1] :
                dp[i] = dp[i-1] + j
                break

print(sum(dp))