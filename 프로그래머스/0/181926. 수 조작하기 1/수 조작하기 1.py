def solution(n, control):
    for con in control:
        if con == "w":
            n += 1
        elif con == "s":
            n -= 1
        elif con == "d":
            n += 10
        elif con == "a":
            n -= 10
    return n