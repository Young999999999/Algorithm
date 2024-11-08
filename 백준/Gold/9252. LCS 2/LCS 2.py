str1 = input()
str2 = input()

dp=["" for i in range(len(str2))]
cost=["" for i in range(len(str2))]

for i in range(len(str1)):
    for j in range(len(str2)-1,-1,-1):
        if str1[i] == str2[j]:
            dp[j] = cost[j] + str1[i]

    MAX = ""
    for j in range(len(str2)):
        cost[j] = MAX
        if len(MAX) < len(dp[j]):
            MAX = dp[j]

result = ""
for i in dp:
    if len(result) < len(i):
        result = i

print(len(result))
print(result)