import heapq

def push(time, jobs, q):
    INF = int(1e9)
    for i in range(len(jobs)):
        s,l = jobs[i]
        
        if time >= s:
            heapq.heappush(q,(l,s))
            jobs[i] = [INF,INF]

    
def solution(jobs):
    cnt = 0
    time = 0
    q=[]
    result = 0
    
    while True:
        push(time,jobs,q)
        
        if q:
            processingTime, publishedAt = heapq.heappop(q)
            time += processingTime
            delay = time - publishedAt
            result += delay
            cnt+=1
        else:
            time += 1
            
        if cnt == len(jobs):
            break
    
    return result // len(jobs)
        
        