def solution(a, b):
    x,y = min(a,b), max(a,b)
    return sum(range(x,y+1))