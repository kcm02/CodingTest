import math

n = int(input())
size = list(map(int,input().split()))
t, p = map(int, input().split())

print(sum(math.ceil(i/t) for i in size))
print(n//p,n%p)