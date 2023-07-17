n,m = map(int,input().split())
list = []
ball = 0

for i in range(n):
    list.append(i+1)

for i in range(m):
    i,j = map(int,input().split())
    ball = list[i-1]
    list[i-1] = list[j-1]
    list[j-1] = ball

for i in range(n):
    print(f'{list[i]} ',end="")