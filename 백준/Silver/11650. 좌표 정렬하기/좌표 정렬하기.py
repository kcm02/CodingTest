n = int(input())
points = sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x: (x[0],x[1]))

for x,y in points:
    print(f'{x} {y}')