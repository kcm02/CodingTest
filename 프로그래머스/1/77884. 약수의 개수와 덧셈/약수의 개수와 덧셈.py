def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def solution(left, right):
    total = 0
    for i in range(left, right + 1):
        if count_divisors(i) % 2 == 0:
            total += i
        else:
            total -= i
    return total