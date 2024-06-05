import math

def solution(num_list):
    # 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return
    return (1 if pow(sum(num_list),2) > math.prod(num_list) else 0)