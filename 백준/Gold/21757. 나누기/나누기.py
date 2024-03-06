n = int(input())
num = list(map(int,input().split()))

prefixSum = [0] * (n+1)

for i in range(1,n+1):
    prefixSum[i]= prefixSum[i-1]+ num[i-1]
prefixSum.pop(0)


dp=[]

if prefixSum[-1] == 0:
    cnt = prefixSum.count(0) -1
    print(cnt * (cnt-1) * (cnt-2)  // 6)


elif prefixSum[-1] % 4 == 0 :
    first = prefixSum[-1] // 4

    for i in range(n):
        if prefixSum[i] == first or prefixSum[i] == 2*first or prefixSum[i] == 3*first or prefixSum[i] == 4*first:
            dp.append(prefixSum[i])

    dict = {}
    for i in range(5):
        dict[i*first] = 0

    for i in dp :
        if i ==first:
            dict[i] += 1
        else:
            dict[i] = dict[i-first] + dict[i]

    print(dict[first*4])
else:
    print(0)
