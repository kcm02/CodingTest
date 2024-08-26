n,i = map(int,input().split(' '))
handles = sorted([input() for _ in range(n)])
print(handles[i-1])