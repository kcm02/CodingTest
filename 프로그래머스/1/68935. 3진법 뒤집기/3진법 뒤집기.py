def solution(n):
    base_3 = ''
    
    while n > 0:
        base_3 = str(n % 3) + base_3
        n = n // 3
        
    for i,x in enumerate(base_3):
        n += 3**i * int(x)
        
    return n