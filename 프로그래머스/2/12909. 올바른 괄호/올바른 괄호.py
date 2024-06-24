def solution(string):
    stack = []
    
    for s in string:
        try:
            if s == "(":
                stack.append(s)
            else:
                stack.pop()
        except:
            return False
    
    return not(len(stack))