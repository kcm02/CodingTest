def solution(arr, divisor):
    return sorted(i for i in arr if not i % divisor) or [-1]