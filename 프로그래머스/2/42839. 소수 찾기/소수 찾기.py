def judgePrimeNum(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    candidates= set()
    ban = [0] * len(numbers)
    
    def backtrack(num, cnt):
        if cnt == len(numbers):
            return

        for idx,i in enumerate(ban):
            if i == 0:
                num.append(numbers[idx])
                candidates.add(int("".join(num)))
                ban[idx] = 1
                backtrack(num, cnt+1)
                ban[idx] = 0
                num.pop()
                
    backtrack([],0)
    
    for num in candidates:
        if judgePrimeNum(num):
            print(num)
            answer += 1
    
    return answer