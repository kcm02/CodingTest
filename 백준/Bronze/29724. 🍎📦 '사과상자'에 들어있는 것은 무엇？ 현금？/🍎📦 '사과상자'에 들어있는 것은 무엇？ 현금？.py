n = int(input())
m, g = 0, 0

for i in range(n):
    f, w, h, l = input().split(' ')
    if f == 'A':
        a = (int(w) // 12) * (int(h) // 12) * (int(l) // 12)
        m += a * 4000
        g += 1000 + (a * 500)
    else:
        g += 6000
        
print(g)
print(m)