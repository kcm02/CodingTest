from itertools import combinations
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    result = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            result += 1
    return result