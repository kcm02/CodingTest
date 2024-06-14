def is_composite(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False

def solution(n):
    count = 0
    for i in range(1, n + 1):
        if is_composite(i):
            count += 1
    return count