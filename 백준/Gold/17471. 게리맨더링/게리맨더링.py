
# i) 입력 형식 받고
# i) 1...n개 집합 경우의 수 다 구한다.
# i) 집합 실제로 만들어 질 수 있는지 검사한다. 어떻게 ? dfs or bfs로 연결 가능한지 구한다.
    # i) 집합 가능하다면 반대편 집합을 구해서 검사해본다.
    # ii) 집합이 불가능하다면 다음 집합이 가능한지 순회한다.
# ii) 인구수를 비교한다

n = int(input())
cost = list(map(int,input().split()))
graph = [[] for i in range(11)]

for s in range(1,n+1):
    l = list(map(int,input().split()))
    for e in l[1:]:
        graph[s].append(e)

set = [[] for i in range(11)]
elements =[]

def recursive(cnt,idx):
    if cnt == limit:
        set[limit].append(elements[:])

    for i in range(idx,n+1):
        elements.append(i)
        recursive(cnt+1,i+1)
        elements.pop()

for limit in range(1,n):
    recursive(0,1)

INF = 100000000000
answer = [INF]

cnt = [0,0]
node = [[],[]]
def dfs(flag,now, s):
    s.remove(now)
    cnt[flag] += 1

    for next in graph[now]:
        if next in s:
            dfs(flag,next,s)


def getAnotherSet(set):
    l = []
    for i in range(1,n+1):
        if i not in set:
            l.append(i)
    return l

for i in range(1,n):
    for s in set[i]:

        flag = 0
        cnt[flag] = 0
        node1 = s[:]
        dfs(flag,s[0], s)



        # 집합 가능
        if cnt[0] == i:

            flag = 1
            anotherSet = getAnotherSet(node1)
            cnt[flag] = 0
            node2 = anotherSet[:]
            dfs(flag,anotherSet[0], anotherSet)


            if cnt[flag] == len(node2):
                total1 = 0
                total2 = 0
                for j in node1:
                    total1 += cost[j-1]
                for j in node2:
                    total2 += cost[j-1]

                answer[0] = min(answer[0], abs(total1 - total2))


if answer[0] == INF:
    print(-1)
else:
    print(answer[0])

