import sys
input =sys.stdin.readline

#인풋 예시

"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""

INF = int(1e9)

n= int(input())
m= int(input())
matrix = [[INF for i in range(n)] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    if matrix[a-1][b-1] == INF :
        matrix[a - 1][b - 1] = c
    else: #출발지 노드와 도착지 노드를 연결하는 선분이 이미 있다면
        if matrix[a-1][b-1] > c : #더 작은 값인 c를 넣어준다
            matrix[a-1][b-1] = c

for i in range(n): # 출발지 노드와 도착지 노드가 본인일 때 비용을 0으로 ex) 0 -> 0 , 1-> 1
    matrix[i][i]=0

#거쳐가는 노드
for i in range(n):
    #출발지 노드
    for j in range(n):
        #도착 노드
        for k in range(n):
            if matrix[j][k] > matrix[j][i] + matrix[i][k]:
                matrix[j][k] = matrix[j][i] + matrix[i][k]


for i in range(n):
    for j in range(n):
        if matrix[i][j] == INF:
            matrix[i][j] = 0
        print(matrix[i][j], end=' ')
    print()
