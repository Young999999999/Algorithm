from collections import deque
t,n,d,k = map(int,input().split())
teas = list(map(int,input().split()))
teas.sort()
dict = {}
cnt = 0
for tea in teas:
    cnt += 1
    dict[tea] = cnt

teas = list(dict.keys())
num = list(dict.values())
teas.append(int(1e10))
num.append(int(1e10))

left = {}
pre = -1
lines = []
for i in teas:
    left[i] = pre
    pre = i

def judge(now):
    l = 0
    r = len(teas)
    for i in range(21):
        mid = (l+r) // 2
        if teas[mid] < now+d:
            l = mid
        elif teas[mid] >= now+d:
            r = mid

    return l

items = [0] * (len(teas))
for i in range(len(teas)-1):
    e = judge(teas[i])
    s =  i-1
    items[i] = num[e] - num[s]
    if s == -1:
        items[i] = num[e]

dp=[[0] * len(teas) for i in range(k+1)]
for cnt in range(1,k+1):
    dp[cnt][0] = 1
    for i in range(len(teas)-1):
        idx = judge(teas[i])
        dp[cnt][idx] = max(dp[cnt][idx],dp[cnt-1][i-1]+items[i])

    for i in range(len(teas)-1):
        dp[cnt][i] = max(dp[cnt][i],dp[cnt][max(0,i-1)])


MAX = max([max(i) for i in dp])

# for i in dp:
#     print(i)
print(MAX)






