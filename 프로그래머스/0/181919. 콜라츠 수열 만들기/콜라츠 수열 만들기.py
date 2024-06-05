def solution(n):
    result = []
    while True:
        result.append(n)
        if n == 1: break
        n = (3 * n + 1 if n % 2 else n / 2)
    return result