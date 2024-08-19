def count_divisors(n):
    count = 0
    for i in range(1,n):
        if not n % i:
            count += 1
    return count % 2

def solution(left, right):
    total = 0
    for i in range(left,right+1):
        total += i if count_divisors(i) else -i
    return total