from itertools import combinations

def solution(number):
    comb = list(combinations(number, 3))
    return sum(1 for i in comb if sum(i) == 0)