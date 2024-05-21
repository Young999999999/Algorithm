def solution(phone_book):
    answer = True
    
    hash = {}
    for i in range(1,21):
        hash[i] = {}
        
    for num in phone_book:
        hash[len(num)][num] = 1
    
    for check in phone_book:
        for i in range(1,len(check)):
            if hash[i].get(check[:i]) != None:
                return False
            
        
    
    return answer