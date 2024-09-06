#rotateDir이 참이면 시계 방향 거짓이면 반시계 방향
def rotate():
    for target,rotateDir in rotateList:
        #시계 방향
        if rotateDir:
            tmp = [0] * 8
            tmp[0] = wheel[target][-1]
            for i in range(7):
                tmp[i+1] = wheel[target][i]
            wheel[target] = tmp[:]

        #반시게 방향
        else:
            tmp = [0] * 8
            tmp[-1] = wheel[target][0]
            for i in range(7):
                tmp[i] = wheel[target][i+1]
            wheel[target] = tmp[:]

def judge(now,dir,rotateDir):
    if dir == -1:
        if now == 0:
            return
        if wheel[now][6] != wheel[now-1][2]: #서로 극이 다르면 다른 방향으로 회전 시켜야함
            rotateList.append((now-1,not rotateDir))
            judge(now-1,dir,not rotateDir)

    if dir == 1:
        if now == 3:
            return
        if wheel[now][2] != wheel[now+1][6]:
            rotateList.append((now+1,not rotateDir))
            judge(now+1,dir,not rotateDir)


def getScore():
    global score

    for i in range(4):
        if wheel[i][0] == 1: #톱니의 12시 방향이 N극일 때
            score += 2**i



score = 0
#N은 0 S는 1
wheel = [list(map(int,list(input()))) for i in range(4)]
n = int(input())
for i in range(n):
    rotateList = []
    rotateDir = None
    target,dir = map(int,input().split())
    if dir == 1:
        rotateDir = True

    if dir == -1 :
        rotateDir = False
    target-=1
    rotateList.append((target, rotateDir))
    judge(target,-1,rotateDir)
    judge(target,1,rotateDir)
    rotate()
    rotateList = list(set(rotateList))


getScore()
print(score)









