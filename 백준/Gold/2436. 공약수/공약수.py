GCD,LCM = map(int,input().split())

def uclid(a,b):

    if b == 0:
        return a

    return uclid(b,a%b)



A = 0
B = 1
MIN = [100000000000000,100000000000000]

while B > A :

    A += GCD

    if LCM % A != 0 :
        continue


    a = A//GCD
    b = LCM // A

    if uclid(a,b) != 1: #a,b 가 서로소라면
        continue

    B = b * GCD

    if A+B < sum(MIN) :

        MIN = [A,B]


print(*MIN)




