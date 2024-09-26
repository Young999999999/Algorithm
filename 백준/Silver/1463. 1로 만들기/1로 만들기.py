x = int(input())

INF = 1e9
dp = [INF] * (x+1)

dp[1] = 0
for i in range(1,x+1):
    for j in [i*3,i*2,i+1] :
        if j <= x:
            dp[j]= min(dp[i] + 1,dp[j])

print(dp[x])