t = int(input())

for i in range(t):
    r,s = input().split()
    for i in s:
        print(int(r) * i,end='')
    print()