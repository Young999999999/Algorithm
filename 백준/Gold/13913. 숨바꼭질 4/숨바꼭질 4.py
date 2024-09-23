import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

def print_path(k): # 패스 출력 함수
    if k > -1:
        if graph[k]>-1:
            route.append(graph[k])
        else:
            for i in range(len(route)-1,-1,-1): #패스의 길이 만큼 반복
                print(route[i],end=' ')
            return
        print_path(graph[k])
    return

def BFS(node):
    q=deque()
    q.append(node)
    visited[node]=True
    while(q):
        num=q.popleft()
        if num == k : #start 와 end가 같을 경우
            print(cnt[num])
            print(k)
            return

        for i in (num-1,num+1,2*num): # 초당 거리 변화의 경우의 수
            if i<0 or i>100000:
                continue
            if i == k:
                print(cnt[num]+1)
                graph[k] = num
                print_path(k)
                print(k, end=' ')
                return
            if not visited[i]:
                cnt[i]=cnt[num]+1
                graph[i]= num
                q.append(i)
                visited[i]=True


    return

route=[]
graph=[-1]*100001
n,k =map(int,input().split())
cnt =[0] * 100001
visited = [False] * 100001
BFS(n)
