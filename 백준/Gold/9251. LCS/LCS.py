
str1 = input()
str2 = input()

dp=[0]*len(str2)
cost = [0]*len(str2)

for i in range(len(str1)):
    for j in range(len(str2)-1,-1,-1):
        if str1[i] == str2[j]:
            dp[j] = cost[j] + 1

    MAX = 0
    for j in range(len(str2)):
        cost[j] = MAX
        MAX = max(dp[j],MAX)

print(max(dp))