def solution(a, b):
    x,y = min(a,b), max(a,b)
    return sum(i for i in range(x,y+1))