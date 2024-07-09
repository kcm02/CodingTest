def solution(s):
    answer = []
    last_seen = {}
    
    for i, char in enumerate(s):
        if char in last_seen:
            answer.append(i - last_seen[char])
        else:
            answer.append(-1)
        last_seen[char] = i
    
    return answer