def solution(arr, divisor):
    result = [i for i in arr if i % divisor == 0]
    return sorted(result) if result else [-1]