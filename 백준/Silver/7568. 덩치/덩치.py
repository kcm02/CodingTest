n = int(input())
body = [tuple(map(int, input().split())) for _ in range(n)]

for i,x in enumerate(body):
    x,y = x
    count = 1
    for p,q in body:
        if x < p and y < q:
            count += 1
    print(count, end=" ")