
def getViewCount(now):
    return max(0,buildings[now]-max(buildings[now-2],buildings[now-1],buildings[now+1],buildings[now+2]))

for i in range(10):
    cnt = 0
    n = int(input())
    buildings = list(map(int,input().split()))
    for idx in range(n):
        if buildings[idx]:
            cnt += getViewCount(idx)

    print("#{} {}".format(i+1,cnt))




