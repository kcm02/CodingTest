a = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
    a[i] = list(map(int,input().split()))

max_val = max(map(max, a))

for i in range(9):
    for j in range(9):
        if max_val == a[i][j]:
            print(max_val)
            print(f'{i+1} {j+1}')