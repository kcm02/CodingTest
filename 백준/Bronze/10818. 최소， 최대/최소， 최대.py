n = int(input())
list = list(map(int,input().split()))
max = list[0]
min = list[0]

for i in range(n):
    if i>0:
        if list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]

print(f'{min} {max}')