def solution(s):
    count = 0
    index = 0
    
    while index < len(s):
        x = s[index]
        same = 0
        diff = 0
        
        while index < len(s):
            if s[index] == x:
                same += 1
            else:
                diff += 1
            
            if same == diff:
                break
            index += 1
            
        count += 1
        index += 1
    
    return count
