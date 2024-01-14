from collections import deque

import sys
input= sys.stdin.readline

def isTrue(x,y): #True가 될 수 있다면 True 벽밖에 못 가면 벽이 됨
    judge = []

    vector = [[i, i] for i in range(1, K + 1)]
    vector.append([1, 0])
    vector.append([0, 1])


    for dy,dx in vector:
        next_y = y+dy
        next_x = x+dx

        if 0 <= next_y < N and 0 <= next_x < M : #바운드 초과하지 않았을 때
            if not matrix[next_y][next_x] == '#' and not victory =='#': # 벽이 아니고
                judge.append(victory[next_y][next_x])


    if len(judge) != 0 and not True in judge : #F로만 보낼 수 있다면
        victory[y][x] = True
        setFalse(x,y)

    elif len(judge) == 0:
        victory[y][x] = '#'


def setFalse(x,y):

    for dy,dx in vector:
        next_y = y+dy
        next_x = x+dx


        if 0 <= next_y < N and 0 <= next_x < M : #바운드 초과하지 않았을 때
            if not matrix[next_y][next_x] == '#' and not victory =='#': # 벽이 아닐 때, 실제 벽과 논리적 벽
                victory[next_y][next_x]= False




def judge_win(x,y):
    vector = [[i, i] for i in range(1, K + 1)]
    vector.append([1, 0])
    vector.append([0, 1])

    judge=[]
    for dy,dx in vector:
        next_y = y+dy
        next_x = x+dx

        if 0 <= next_y < N and 0 <= next_x < M : #바운드 초과하지 않았을 때
            if not matrix[next_y][next_x] == '#' and not victory =='#': # 벽이 아니고
                judge.append(victory[next_y][next_x])

    if len(judge) != 0 and True in judge :
        print("First")
    else:
        print("Second")



N,M,K = map(int,input().split())

#vector 설정
vector = [[-i,-i] for i in range(1,K+1)]
vector.append([-1,0])
vector.append([0,-1])


matrix = []

for i in range(N):
    matrix.append(list(input().strip()))

victory =[[0 for i in range(M)] for j in range(N)]

victory[N-1][M-1] = True
setFalse(M-1,N-1)


for y in range(N-1,-1,-1):
    for x in range(M-1,-1,-1):

        if victory[y][x] == 0 and not matrix[y][x] == '#': #아직 True와 False가 결정되지 않은 경우

            isTrue(x,y)


Q = int(input())

for i in range(Q):
    start_y,start_x = map(int,input().split())

    judge_win(start_x-1,start_y-1)

