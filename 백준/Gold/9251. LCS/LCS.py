A = input()
B = input()
dp =[0] * 1001
trace=[i for i in range(1001)]

path = []
def getPath(node,cnt):
    if cnt == 0:
        return
    path.append(B[node])

    getPath(trace[node],cnt-1)

for i in range(len(A)):
    MAX = 0
    idx = 0
    for j in range(len(B)):
        # 내가 갱신한 것이 아니라 남이 갱신 한 거라면 MAX 카운트를 바꿔준다.
        if A[i] == B[j]:
            if dp[j] > MAX:
                MAX = dp[j]
                idx = j
            else:
                dp[j] = MAX+1
                trace[j] = idx
        else:
            if MAX < dp[j]:
                MAX = dp[j]
                idx = j

result = 0
idx = 0
for i in range(1001):
    if result < dp[i]:
        result = dp[i]
        idx = i

print(result)
getPath(idx,result)
