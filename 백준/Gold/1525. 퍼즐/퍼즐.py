from collections import deque
import sys
q=deque()
input = sys.stdin.readline


 #상 하 좌 우

#입력
init_str = "".join([input().replace(" ","").strip() for i in range(3)])

vector = [[-1,0],[1,0],[0,1],[0,-1]]
q.append(init_str)
dict={}
dict[init_str] = 0
if init_str == "123456780":
    print(0)
    exit(0)
#입력 종료
cnt = 0
while q:
    puzzle=q.popleft()
    idx = puzzle.index('0')
    y, x = idx // 3, idx % 3

    for i in vector :
        dy, dx = i
        if y + dy == 3 or x + dx == 3 or y + dy == -1 or x + dx == -1:  # 범위 초과
            continue
        search_idx=3*(y+dy)+x+dx #
        list_puzzle =list(puzzle)
        #값을 스위칭
        list_puzzle[idx],list_puzzle[search_idx] = list_puzzle[search_idx],list_puzzle[idx]
        list_to_str="".join(list_puzzle)
        if not list_to_str in dict:
            q.append(list_to_str)
            dict[list_to_str]=dict[puzzle]+1
            if list_to_str == "123456780":  # goal에 도달했다면 출력후 프로그램 종료
                print(dict[list_to_str])
                exit(0)
print(-1)




