import itertools

def solution(babbling):
    result = []
    for i in range(1, len(["aya", "ye", "woo", "ma"]) + 1):
        for combo in itertools.permutations(["aya", "ye", "woo", "ma"], i):
            result.append(''.join(map(str, combo)))
            
    return sum(1 for x in babbling if x in result)