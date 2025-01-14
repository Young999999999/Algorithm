def solution(prices):
    
    def convert(x):
        return -x
    
    prices = list(map(convert,prices))
    stack = [(100000,0)]
    answer = []
    
    
    for i in range(len(prices) - 1,-1,-1):
        price,idx = prices[i],len(prices)-1-i
        
        if stack[-1][0] <= price:
            while stack:
                if stack[-1][0] <= price:
                    stack.pop()
                else:
                    break
            stack.append((price,idx))
        else:
            stack.append((price,idx))
        answer.append(stack[-1][1]-stack[-2][1])
        
        
    return answer[::-1]