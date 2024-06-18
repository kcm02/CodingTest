import itertools

def solution(lines):
    flat = list(itertools.chain.from_iterable(lines))
    result = [0 for _ in range(max(flat) - min(flat) + 1)]
    
    for a, b in lines:
        for i in range(a, b):
            result[i - min(flat)] += 1
    
    return sum(1 for count in result if count > 1)