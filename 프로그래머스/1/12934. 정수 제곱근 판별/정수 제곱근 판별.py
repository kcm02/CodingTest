def solution(n):
    sqrt_n = int(n ** 0.5)
    return (sqrt_n + 1) ** 2 if sqrt_n * sqrt_n == n else -1