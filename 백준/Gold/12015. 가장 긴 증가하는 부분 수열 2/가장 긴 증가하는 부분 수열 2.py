# 맨 왼쪽의 T의 값을 바꿔줌  dp[True_INDEX] = new_value
# 맨 오른쪽값이 F라면 새로운 값 append


# 이 과정을 이분탐색으로 바꿔야함.
# O(nlogn)으로 나올 수 있도록
# dp 리스트는 증가순임이 보장되어 있음
# 증가순이 보장되어 있기에 이분탐색이 가능
# 각 자리의 최소로 들어갈 수 있는 수가 들어감


n = int(input())
num = list(map(int,input().split()))
dp=[num[0]]

for i in range(n):
    cnt = 0


    s = 0
    e = len(dp)-1

    for j in range(20):
        idx = (s + e) // 2
        if dp[idx] >= num[i]:
            e = idx-1
        else:
            s = idx+1

    if s == len(dp):
        dp.append(num[i])
    else:
        dp[s] = num[i]

print(len(dp))





