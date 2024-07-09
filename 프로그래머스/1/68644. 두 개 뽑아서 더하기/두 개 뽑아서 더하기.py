from itertools import combinations

def solution(numbers):
    comb = list(combinations(numbers, 2))
    return sorted(set(sum(pair) for pair in comb))