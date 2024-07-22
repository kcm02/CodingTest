def solution(ingredient):
    count = 0
    hamburger = [1,2,3,1]
    stack = []

    for item in ingredient:
        stack.append(item)
        if len(stack) >= 4 and stack[-4:] == hamburger:
            count += 1
            for _ in range(4):
                stack.pop()
    
    return count