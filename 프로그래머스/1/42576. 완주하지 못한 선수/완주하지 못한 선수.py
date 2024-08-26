def solution(participant, completion):
    name_count = {}
    
    for name in participant:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    
    for name in completion:
        name_count[name] -= 1
    
    return "".join(k for k,v in name_count.items() if v > 0)