a = int(input())
b = int(input())
c = int(input())

n = str(a * b * c)

for i in range(10):
    print(n.count(str(i)))