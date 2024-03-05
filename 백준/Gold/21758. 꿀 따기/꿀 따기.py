num = int(input())
honey = list(map(int,input().split()))

# 아래의 세 가지중 max를 취해주면된다
#
# i) bee bee house -> 2 * SUM - 2*bee(1) - 2*bee(2) - sequence(1~2)
# ii) bee house bee -> 이때 house는 무조건 가장 큰 값이여야함  -> bee, house, bee SUM - bee(1) -bee(2) + house
# iii) house bee bee -> 2 * SUM - 2*bee(1) - 2*bee(2) - sequence(1~2)
# i과 iii는 사실상 같은 케이스 list를 reverse 시키고 같은 과정을 반복하자

SUM = sum(honey)
prefixSum = [0] * (num+1)

for i in range(num):
    prefixSum[i+1] = prefixSum[i] + honey[i]


def case1():
    global MAX

    for i in range(1,num-1):
        result = 2*SUM - prefixSum[i+1] - honey[0] -honey[i]
        MAX=max(result,MAX)

def case2():
    global MAX
    MAX = max(MAX,SUM + max(honey) - honey[0] - honey[num-1])


MAX = 0
# i) 의 경우
case1()

# ii)의 경우
case2()

#iii) 의 경우
honey.reverse()
prefixSum = [0] * (num+1)
for i in range(num):
    prefixSum[i+1] = prefixSum[i] + honey[i]
case1()

print(MAX)