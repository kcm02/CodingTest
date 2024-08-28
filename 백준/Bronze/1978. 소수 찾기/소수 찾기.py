def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

n = int(input())
l = list(map(int,input().split()))
count = 0

for i in l:
    if is_prime(i):
        count += 1

print(count)