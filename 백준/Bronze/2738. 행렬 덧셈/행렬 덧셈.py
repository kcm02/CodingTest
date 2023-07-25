n,m = map(int,input().split())

a = [[0 for col in range(m)] for row in range(n)]
b = [[0 for col in range(m)] for row in range(n)]

for i in range(n):
  a[i] = list(map(int,input().split()))

for i in range(n):
  b[i] = list(map(int,input().split()))

for i in range(n):
  for j in range(m):
    print(a[i][j]+b[i][j],end=' ')
  print()