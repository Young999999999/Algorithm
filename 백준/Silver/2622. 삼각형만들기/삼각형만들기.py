n = int(input())

if n % 3 == 0 :
    longest = n // 3
else:
    longest = n // 3 + 1

# a+b > c
cnt = 0

while n - longest > longest:
    for i in range(1,longest+1):
        if n -longest - i <= longest  and n-longest - i >= i :
            cnt+=1

    longest += 1

print(cnt)