import sys
import heapq
input = sys.stdin.readline

q=[]
meeting = []
cnt = 1
for i in range(int(input())):
    meeting.append(list(map(int,input().split())))

meeting.sort()
heapq.heappush(q,meeting[0][1])

for s,e in meeting[1:]:
    minE = heapq.heappop(q)
    if minE <= s:
        heapq.heappush(q,e)
    else:
        cnt += 1
        heapq.heappush(q,e)
        heapq.heappush(q,minE)

print(cnt)









