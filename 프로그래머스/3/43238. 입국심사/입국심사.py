def solution(n, times):
    answer = 0
    
    def count(limit, times):
        result = 0
        for i in times:
            result += limit // i
        return result
    
    s = 0
    e = 10 ** 15
    

    for i in range(50):
        mid = (s + e) // 2
        throughput = count(mid,times)
        
        if throughput >= n:
            e = mid
        else:
            s = mid
    
    return e