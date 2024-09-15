import sys
from collections import deque
input = sys.stdin.readline
def BFS(node):
    q=deque()
    tp=node
    visited[tp] = True
    q.append(node)

    for i in range(1,10000):
        tp *=2
        if tp <= 100000:
            q.append(tp)
            visited[tp]=True
        else :
            break

    while(q):
        num = q.popleft()
        if  num== k :
            print(cnt_arr[num])
            break


        if num-1 >= 0:
            num_i =num-1
            if not visited[num_i] :
                cnt_arr[num_i] = cnt_arr[num]+1
                visited[num_i]=True
                q.append(num_i)
            tp = num_i
            for i in range(1, 10000):
                tp *= 2
                if tp <= 100000 and not visited[tp]:
                    q.append(tp)
                    visited[tp] = True
                    cnt_arr[tp] = cnt_arr[num_i]
                if tp > 100000:
                    break


        if num+1 <= 100000:
            num_ii = num+1
            if not visited[num_ii] :
                cnt_arr[num_ii] = cnt_arr[num]+1
                visited[num_ii]=True
                q.append(num_ii)
            tp = num_ii
            for i in range(1, 10000):
                tp *=2
                if tp <= 100000 and not visited[tp]:
                    q.append(tp)
                    visited[tp] = True
                    cnt_arr[tp] = cnt_arr[num_ii]
                if tp > 100000:
                    break


    return 0
n,k =map(int,input().split())
cnt_arr = [0] * 100001
visited=[False]*100001
BFS(n)

