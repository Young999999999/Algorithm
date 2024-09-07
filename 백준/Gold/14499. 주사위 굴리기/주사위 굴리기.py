def moveEast(dice):
    return [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]

def moveWest(dice):
    return [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]

def moveNorth(dice):
    return [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]

def moveSouth(dice):
    return [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]

def copy(x,y):
    if MAP[y][x] == 0:
        MAP[y][x] = dice[0]
    else:
        dice[0] = MAP[y][x]
        MAP[y][x] = 0

N,M,y,x,K = map(int,input().split())
MAP =[list(map(int,input().split())) for i in range(N)]
dice = [0,0,0,0,0,0]
#동1 서2 북3 남4
dir = list(map(int,input().split()))
for vector in dir:
    if vector  == 1:
        x += 1
        y += 0
        if 0 <= x < M:
            dice = moveEast(dice)
            copy(x,y)
            print(dice[5])
        else:  # 범위 초과시 rollback
            x -= 1

    if vector == 2:
        x += -1
        y += 0
        if 0 <= x < M:
            dice = moveWest(dice)
            copy(x, y)
            print(dice[5])
        else:  # 범위 초과시
            x += 1

    if vector == 3:
        x += 0
        y += -1
        if 0 <= y < N:
            dice = moveNorth(dice)
            copy(x, y)
            print(dice[5])
        else:  # 범위 초과시
            y += 1

    if vector == 4:
        x += 0
        y += 1
        if 0 <= y < N:
            dice = moveSouth(dice)
            copy(x, y)
            print(dice[5])
        else:  # 범위 초과시
            y -= 1

