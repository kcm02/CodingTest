def solution(prices):
    l = len(prices)
    answer = [0] * l
    stack = []
    
    for i in range(l):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        
        stack.append(i)
        
    while stack:
        top = stack.pop()
        answer[top] = l - 1 - top
                
    return answer