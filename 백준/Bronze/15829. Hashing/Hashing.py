l = int(input())
s = input()
n = 0
sum = 0

for i,x in enumerate(s):
    sum += (ord(x)-96) * (31 ** n)
    n += 1

print(sum)