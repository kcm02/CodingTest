n = int(input())
for _ in range(n):
    l = list(map(str,input().split('X')))
    print(sum([sum([int(j+1) for j in range(len(i))]) for i in l]))