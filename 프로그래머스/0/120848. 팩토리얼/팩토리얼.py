def solution(n):
    num = 1
    factorial = 1
    while factorial <= n:
        num += 1
        factorial *= num
    return num-1