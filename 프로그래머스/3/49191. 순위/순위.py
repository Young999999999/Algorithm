import sys 

def solution(n, results):
    answer = 0
    graph = [[] for i in range(n+1)]
    reverse_graph= [[] for i in range(n+1)]
    
    for s,e in results:
        graph[s].append(e)
        reverse_graph[e].append(s)
    
    
    def dfs(now,visited,graph):
        visited[now] = 1
        
        for next in graph[now]:
            if not visited[next]:
                dfs(next,visited,graph)
    
    for i in range(1,n+1):
        visited = [0 for i in range(n+1)]
        dfs(i, visited, graph)
       
        cnt = sum(visited)
        
        visited = [0 for i in range(n+1)]
        dfs(i, visited,reverse_graph)
        cnt += sum(visited)
        
        if n == cnt - 1:
            answer += 1
            
        
    return answer
