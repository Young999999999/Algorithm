def solution(n, costs):    
    answer = 0
    parents = [-1 for i in range(n)]
    
    def find(n):
        if parents[n] == -1:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def merge(a,b):
        a = find(a)
        b = find(b)
        
        if a == b:
            return False
        
        a,b = max(a,b), min(a,b)
        parents[a] = b
        return True
        
    costs.sort(key=lambda x:x[2])
    
    for a,b,cost in costs:
        if merge(a,b):
            answer += cost
        
        cnt = 0
        for i in parents:
            if i== -1 :
                cnt += 1
        
        if cnt == 1:
            return answer
        
        
    
    
    
    return answer