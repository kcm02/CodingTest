from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for size in course:
        comb_dict = defaultdict(int)
        
        for order in orders:
            comb_list = list(combinations(sorted(order), size))
            for comb in comb_list:
                comb_dict[''.join(comb)] += 1
        
        if comb_dict:
            max_count = max(comb_dict.values())
            if max_count >= 2:
                answer += [comb for comb, count in comb_dict.items() if count == max_count]
    
    return sorted(answer)