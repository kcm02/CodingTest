def is_valid(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for c in s:
        if c in matching.values():
            stack.append(c)
        else:
            if not stack or stack.pop() != matching[c]:
                return False
                
    return not stack

def solution(s):
    count = 0
    temp = list(s)
    
    for _ in range(len(s)):
        if is_valid(temp):
            count += 1
        first_char = temp.pop(0)
        temp.append(first_char)
    
    return count