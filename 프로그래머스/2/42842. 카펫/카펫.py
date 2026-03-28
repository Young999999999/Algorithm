def solution(brown, yellow):
    answer = []
    
    for h in range(3,5001):
        for w in range(3,5001):
            b = 2*w + 2*h -4
            y = (w-2) * (h-2)
            
            if [b,y] == [brown,yellow]:
                return [w, h]

    return answer
