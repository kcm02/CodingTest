def solution(num, total):
    if num % 2: 
        start = total // num - (num//2)
    else: 
        start = total // num - (num//2) + 1
        
    return list(range(start, start + num))