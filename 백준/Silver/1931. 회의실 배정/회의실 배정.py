# 종료시간을 기준으로 sort
import sys
input = sys.stdin.readline
n = int(input())
arr = [[0]* 2 for i in range(n)]

for i in range(n):
    arr[i][0],arr[i][1] = map(int,input().split())

arr = sorted(arr, key=lambda x:(x[1],x[0]))
cnt =1
arr_key=[]
arr_key=arr[0] #초기값 설정
#print(arr)
for i in range(1,n):
    if arr_key[1] > arr[i][0] :
        continue
    if arr_key[1] <= arr[i][0]:
        arr_key = arr[i]
        cnt+=1
print(cnt)
