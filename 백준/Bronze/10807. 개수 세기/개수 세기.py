n = int(input())
count = 0

list = list(map(int,input().split()))

v = int(input())

for i in range(len(list)):
    if list[i] == v:
        count += 1

print(count)