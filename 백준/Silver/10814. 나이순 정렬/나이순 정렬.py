n = int(input())
users = sorted([tuple(map(str,input().split())) for _ in range(n)],key= lambda x: int(x[0]))

for age,name in users:
    print(f'{age} {name}')