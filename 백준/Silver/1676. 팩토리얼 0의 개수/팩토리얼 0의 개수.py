import math

n = int(input())
f = str(math.factorial(n))[::-1]

for i,x in enumerate(f):
    if x != '0':
        print(i)
        break