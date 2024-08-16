def solution(arr, divisor):
    result = sorted(i for i in arr if not i % divisor)
    return result if result else [-1]