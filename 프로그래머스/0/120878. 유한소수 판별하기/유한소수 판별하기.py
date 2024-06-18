import math

def solution(a, b):
    gcd = math.gcd(a, b)
    r_denom = b // gcd
    
    while r_denom % 2 == 0:
        r_denom //= 2
    while r_denom % 5 == 0:
        r_denom //= 5
        
    return 1 if r_denom == 1 else 2