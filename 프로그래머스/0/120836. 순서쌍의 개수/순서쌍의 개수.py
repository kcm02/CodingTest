def solution(n):
    return len([(x,n//x) for x in range(1,n+1) if x*(n//x) == n])