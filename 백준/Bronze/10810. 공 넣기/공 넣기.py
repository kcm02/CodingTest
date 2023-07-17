n,m = map(int,input().split())
list = [0 for i in range(n)] # 0 0 0 0 0

for i in range(m):
    i,j,k = map(int,input().split())
    for l in range(n):
        if i-1 <= l and l <= j-1:
            list[l] = k

for i in range(n):
    print(f'{list[i]} ',end="")