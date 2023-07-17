n = int(input())
list = list(map(int,input().split()))
max = list[0]
total = 0

for i in range(n):
    if list[i]>max:
        max = list[i]

for i in range(n):
   total += list[i]/max*100

print(total/n)