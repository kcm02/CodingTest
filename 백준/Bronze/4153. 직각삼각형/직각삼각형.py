while True:
    l = sorted(list(map(int,input().split())))
    a, b, c = l[0], l[1], l[2]
    if a + b + c == 0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")