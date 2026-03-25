def solution(citations):
    answer = 0
    citations.sort(key=lambda x:-x)
    result = 0
    
    for h in range(10001):
        if len(citations) >= h:
            if citations[h-1] >= h:
                result = h
    
    return result