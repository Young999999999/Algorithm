t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    items = list(map(int,input().split()))

    dp = {}
    for item in items:
        for key in sorted(dp.keys(),reverse=True):
            if key+item in dp:
                dp[key+item] += dp[key]
            else:
                dp[key+item] = dp[key]

        if item in dp:
            dp[item] += 1
        else:
            dp[item] = 1

    if k in dp:
        print("#{} {}".format(_+1,dp[k]))

    else:
        print("#{} {}".format(_+1,0))