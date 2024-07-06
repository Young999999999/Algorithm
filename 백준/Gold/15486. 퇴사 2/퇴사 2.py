
N = int(input())
dp=[0]*1600000
MAX = 0
for i in range(1,N+1):
    t,p = map(int,input().split())

    dp[i+t-1] = max(dp[i+t-1],dp[i-1]+p)

    MAX = max(MAX,dp[i-1])
    dp[i] = max(MAX, dp[i])


print(max(dp[:N+1]))