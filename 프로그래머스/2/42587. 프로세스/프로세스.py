def nextMaxValue(count):
    for i in range(9,0,-1):
        if count[i]:
            return i

def solution(priorities, location):
    answer = 0
    length = len(priorities)
    idx = 0
    result = 0
    count = [0] * 10
    
    for p in priorities:
        count[p] += 1

    while True:
        MAX = nextMaxValue(count)
        
        if priorities[idx] == MAX:
            count[MAX] -= 1
            priorities[idx] = 0
            result += 1
            if location == idx:
                return result
            
            
            
        idx = (idx + 1) % length
    
    
    
    
    
    return answer