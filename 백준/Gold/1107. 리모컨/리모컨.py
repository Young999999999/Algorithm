import sys
input = sys.stdin.readline

#리모컨 숫자를 조합하는 경우의 수 3
#i) 그냥 100에서 +,-만 딸깎 딸깍
#ii) 0~9버튼만 사용
#iii) 0~9 버튼사용 후 +,- 딸깍 딸깎
# 이 세가지중 최소 값
N = input().strip()
M  =int(input())
b = list(map(str,input().split()))
ban = {}

for i in b :
    ban[str(i)] ='hi'

cnt = 100000000000000

for i in range(1000001):
    judge = str(i)
    bit = 0
    for j in judge:  #고장난 버튼이 있는지 확인
        if ban.get(j) != None:
            bit = 1
            break



    if bit == 0: #고장나지 않았다면
        cnt = min(cnt,len(str(i))+abs(int(N)-i))

#그냥 100에서 딸깍 딸깍
cnt =  min(cnt,abs(int(N)-100))
print(cnt)