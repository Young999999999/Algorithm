import sys
input = sys.stdin.readline
n= int(input())

arr  =list(map(int,input().split()))

length = [1]*n

for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[j] > arr[i]:
            length[j] = max(length[j],length[i]+1)

print(max(length))
