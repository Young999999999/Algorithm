import sys
input =sys.stdin.readline

N = int(input())

money = list(map(int,input().split()))
limit = int(input())

def BS(low,up):
    while True:
        target = (low + up)//2 #정수상한선

        sum = 0 # 예산의 총합
        for i in money:
            if i > target: #정수상한선을 넘으면 정수상한선의 값을 넣어줌
                sum+=target
            else:
                sum+=i
                if sum >limit: #이미 sum이 limit를 넘는다면 up을 target-1로 바꿔야한다
                    break #시간초과 방지 break

        if sum == limit:
            print(target)
            sys.exit()

        if sum > limit : #예산을 초과했다면
            up=target-1
            if low>up:
                print(target-1)
                sys.exit()

        elif sum < limit:
            low = target+1
            if low>up:
                print(target)
                sys.exit()


up=max(money)
BS(0,up)