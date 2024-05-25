n,M = map(int,input().split())
memory = list(map(int,input().split()))
cost = list(map(int,input().split()))
dp = [0] * 10001

for i in range(n):
    c = cost[i]
    m = memory[i]

    for j in range(10000,-1,-1):
        if j-c >= 0 :
            if dp[j-c] != 0 :
                dp[j] = max(dp[j-c] +m,dp[j])

    dp[c] = max(dp[c],m)

for i in range(10001):
    if dp[i] >= M:
        print(i)
        break


