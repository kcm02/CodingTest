import math

t = int(input())
        
for i in range(t):
    k = int(input())
    n = int(input())
    print(math.comb(k + n, n - 1))