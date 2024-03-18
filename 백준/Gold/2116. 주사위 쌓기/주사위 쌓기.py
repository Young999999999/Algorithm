import sys
input = sys.stdin.readline

def top(idx):
    if idx == 0 :
        return 5
    elif idx == 5:
        return 0
    elif idx == 1:
        return 3
    elif idx == 3:
        return 1
    elif idx == 2:
        return 4
    elif idx == 4:
        return 2

n = int(input())

dice = []
for i in range(n):
    dice.append(list(map(int,input().split())))


result = 0


for start in range(6):
    SUM = 0
    value = dice[0][start]

    for i in range(n):
        idx =dice[i].index(value)
        topIdx = top(idx)


        # 상 하를 제외한 나머지 4면에서 최대값 찾기.
        candidate = [1,2,3,4,5,6]
        candidate.remove(dice[i][idx])
        candidate.remove(dice[i][topIdx])
        SUM += max(candidate)

        value = dice[i][topIdx]



    result = max(SUM,result)

print(result)
