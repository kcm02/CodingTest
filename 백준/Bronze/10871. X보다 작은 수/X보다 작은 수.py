n,x = map(int,input().split())

a = list(map(int,input().split()))
b = []

for i in range(len(a)):
    if a[i] < x:
        b.append(a[i])

for i in range(len(b)):
    print(f'{b[i]} ', end="")