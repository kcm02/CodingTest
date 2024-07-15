def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += (1 if i == n // i else 2)
    return count

def solution(number, limit, power):
    result = 0
    for i in range(1, number + 1):
        num = count_divisors(i)
        result += (power if num > limit else num)
    return result