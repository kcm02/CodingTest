l = map(int,input().split())
print(sum(i ** 2 for i in l) % 10)