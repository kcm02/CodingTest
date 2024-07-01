def solution(participant, completion):
    hash_table = {}
    
    for name in participant:
        if name in hash_table:
            hash_table[name] += 1
        else:
            hash_table[name] = 1
        
    for name in completion:
        hash_table[name] -= 1
        
    for name in participant:
        if hash_table[name] > 0:
            return name
        
    return null