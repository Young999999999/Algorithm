T = int(input())


def solveSubProblem(coin):

    dp[coin] += 1
    for i in range(coin,10001,1):
        dp[i] += dp[i-coin]


for i in range(T):
    n = int(input())
    coin = list(map(int,input().split()))
    m = int(input())
    dp = [0] * 10001
    for i in coin:
        solveSubProblem(i)

    print(dp[m])


