t = int(input())
for _ in range(t):
    n = int(input())
    cycle = [0] * (n+1)
    graph = list(map(int,input().split()))

    for i in range(1,n+1):
        if cycle[i] == 0:
            trace = {}
            now = i
            isVisited = 0
            while True:
                next = graph[now - 1]
                trace[now] = 1
                if not next in trace and cycle[next] == 0:  # 아직 미방문
                    now = next
                else:  # 방문 한 거라면
                    nodes = list(trace.keys())
                    if not next in trace:
                        isVisited = 1

                    if isVisited == 0 :
                        bit = 0
                        while nodes:
                            node = nodes.pop()
                            if bit == 0:
                                if node == next:
                                    bit = 1
                                cycle[node] = 1
                            else:
                                cycle[node] = -1
                        break
                    else:
                        while nodes:
                            node = nodes.pop()
                            cycle[node] = -1
                        break

    print(cycle.count(-1))
