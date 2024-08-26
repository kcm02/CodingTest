n = int(input())
d,g = 0,n
c = d

while True:
    if c == d:
        d += 1
        if g - d == 1:
            print("Duck")
            break
        c = g
    else:
        g -= 1
        if g - d == 1:
            print("Goose")
            break
        c = d