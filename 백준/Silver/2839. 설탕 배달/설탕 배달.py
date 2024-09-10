def min_bags(N):
    for i in range(N // 5, -1, -1):
        remainder = N - (i * 5)
        if remainder % 3 == 0:
            return i + (remainder // 3)
    return -1

N = int(input())
print(min_bags(N))