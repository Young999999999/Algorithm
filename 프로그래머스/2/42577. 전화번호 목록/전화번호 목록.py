def solution(phone_book):
    answer= True
    map = [set() for i in range(21)]
    
        
    for i in phone_book:
        map[len(i)].add(i)
    
    for i in range(len(phone_book)):
        for j in range(1,len(phone_book[i])):
            str = phone_book[i][:j]
            if str in map[j]:
                answer=False
        
    return answer