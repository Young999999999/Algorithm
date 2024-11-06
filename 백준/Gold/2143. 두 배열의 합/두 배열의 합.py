t = int(input())
int(input())
aList = list(map(int,input().split()))
int(input())
bList = list(map(int,input().split()))
prefixSumA = [0]
prefixSumB = [0]
partialSumA = []
partialSumB = []
cntA = {}
cntB = {}
for i in aList:
    prefixSumA.append(prefixSumA[-1] + i)

for i in bList:
    prefixSumB.append(prefixSumB[-1] + i)

for i in range(len(prefixSumA)):
    for j in range(i+1,len(prefixSumA)):
        value = prefixSumA[j] - prefixSumA[i]
        partialSumA.append(value)
        if value in cntA:
            cntA[value] += 1
        else:
            cntA[value] = 1

for i in range(len(prefixSumB)):
    for j in range(i+1,len(prefixSumB)):
        value = prefixSumB[j] - prefixSumB[i]
        partialSumB.append(value)
        if value in cntB:
            cntB[value] += 1
        else:
            cntB[value] = 1
partialSumA = list(set(partialSumA))
partialSumB = list(set(partialSumB))
result = 0
for numA in partialSumA:
    diff = t-numA
    if diff in cntB:
        result += cntA[numA] * cntB[diff]

print(result)


