import sys
input = sys.stdin.readline

n= int(input())
dp=[0]
arr=[0]

for i in range(n):
    arr.append(int(input()))


dp.append(arr[1]) # dp[1]
if n >=2:
    dp.append(arr[1] + arr[2]) # dp[2]
    for i in range(3,n+1):
        dp.append(max(dp[i-2]+arr[i], dp[i-3] + arr[i-1] + arr[i]))

print(dp[n])

