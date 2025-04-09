n,k = map(int,input().split())

l = list(input())
cnt = 0
for i in range(n):
    if l[i] == 'P':
        for j in range(max(0,i-k),min(n,i+k+1)):
            if l[j] == 'H':
                cnt+=1
                l[j] = 'None'
                break

print(cnt)
