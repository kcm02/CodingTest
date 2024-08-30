n = int(input())
l = sorted(set([input() for _ in range(n)]),key=lambda x: (len(x), x))

for i in range(len(l)):
    print(l[i])