import sys
input = sys.stdin.readline

def greedy(num):
    cnt = 0
    for i in range(n-1,-1,-1):
        cnt += num // coins[i]
        num = num % coins[i]

    return cnt

n = int(input())
coins = list(map(int,input().split()))
dp=[int(1e9)] * (2*coins[-1]+1)
dp[0] = 0
for coin in coins:
    for i in range(coin,2*coins[-1]+1):
        dp[i]=min(dp[i-coin]+1,dp[i])

for i in range(2*coins[-1],coins[0]-1,-1):

    if greedy(i) > dp[i]:
        print("non-canonical")
        exit(0)

print("canonical")