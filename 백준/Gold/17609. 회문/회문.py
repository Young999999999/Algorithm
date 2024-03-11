import sys
input = sys.stdin.readline

# input : 유사 팰린드롬을 판단할 문자열의 앞에서 절반  , 뒤에서 절반
# output : 유사 팰린드롬이면 True 아니면 False

def judge(str1,str2):

    idx = 0
    bit = 1

    str1 = list(str1)
    str2 = list(str2)
    CNT = len(str2)


    while idx < CNT:

        if str1[idx] != str2[idx] and bit == 1: #문자열 삭제
            str2.pop(idx)
            CNT-=1
            bit = 0

        elif str1[idx] == str2[idx]:
            idx+=1
        else:
            return False

    return True




n= int(input())

for i in range(n):
    s = input().strip()

    str1 = s[:len(s)//2]
    str2 = s[len(s)//2:]

    s = s[::-1]

    str3 = s[:len(s) // 2]
    str4 = s[len(s) // 2:]

    if s == s[::-1] :
        print(0)
    elif judge(str1,str2[::-1]) or judge(str3,str4[::-1]):
        print(1)
    else:
        print(2)
