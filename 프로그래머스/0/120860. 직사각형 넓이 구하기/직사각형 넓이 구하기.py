def solution(dots):
    x, y = zip(*dots)
    return (max(x)-min(x)) * (max(y)-min(y))