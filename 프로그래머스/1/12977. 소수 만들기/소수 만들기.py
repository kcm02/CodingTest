from itertools import combinations
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    result = 0
    comb = list(combinations(nums,3))
    for i in comb:
        if is_prime(sum(i)) == True:
            result += 1
    return result