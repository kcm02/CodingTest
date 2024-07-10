def solution(a, b, n):
    num = n
    answer = 0
    while num >= a:
        bottle = num // a
        answer += bottle * b
        num = bottle * b + num % a
    return answer