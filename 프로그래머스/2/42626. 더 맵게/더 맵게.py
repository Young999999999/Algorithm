import heapq

def mix(food1, food2):
    return food1 + 2*food2

def solution(scoville, K):
    q = []

    for s in scoville:
        heapq.heappush(q,s)
    
    for i in range(1000001):
        MIN = heapq.heappop(q)
        if MIN >= K:
            return i
        else:
            if not q:
                return -1
            MIN2 = heapq.heappop(q)
            heapq.heappush(q,mix(MIN,MIN2))

    return -1