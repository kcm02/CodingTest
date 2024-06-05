def solution(nl):
    n = {1:"w", -1:"s" ,10:"d", -10:"a"}
    s = ""
    for i in range(len(nl) - 1):
        s += n[nl[i+1] - nl[i]]
    return s