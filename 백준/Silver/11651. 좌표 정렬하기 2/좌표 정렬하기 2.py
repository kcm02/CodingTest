n = int(input())
points = sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x: (x[1],x[0]))

for x,y in points:
    print(f'{x} {y}')