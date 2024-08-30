l = int(input())
s = input()
m = 1234567891
sum = 0

for i, x in enumerate(s):
    sum = (sum + (ord(x) - 96) * (31 ** i % m)) % m

print(sum)