n,m = map(int,input().split())
list = [i for i in range(1,n+1)]

for i in range(m):
    i,j = map(int,input().split())
    temp = list[i-1:j]
    temp.reverse()
    list[i-1:j] = temp

for i in range(n):
    print(f'{list[i]} ',end="")