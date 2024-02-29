# 맨 왼쪽의 T의 값을 바꿔줌  dp[True_INDEX] = new_value
# 맨 오른쪽값이 F라면 새로운 값 append


n = int(input())
num = list(map(int,input().split()))
dp=[num[0]]

for i in range(n):
    cnt = 0
    last_index = 1e9
    for j in range(len(dp)-1,-1,-1):
        if dp[j] >= num[i]:
           last_index = j

    if last_index == 1e9 :
        dp.append(num[i])
    else:
        dp[last_index] = num[i]

print(len(dp))







