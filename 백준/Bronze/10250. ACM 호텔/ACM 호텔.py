t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    y = str((n - 1) % h + 1)
    x = str((n - 1) // h + 1).zfill(2)
    print(y + x)