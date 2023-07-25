paper = [[0 for i in range(100)] for row in range(100)]
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            paper[j][k] = 1

count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            count += 1

print(count)