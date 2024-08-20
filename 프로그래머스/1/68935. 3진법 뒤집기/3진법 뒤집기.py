def solution(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    for i,x in enumerate(s):
        n += 3**i * int(x)
    return n