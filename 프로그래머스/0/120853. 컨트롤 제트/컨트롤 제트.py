def solution(s):
    nums = s.split()
    total = 0
    
    for num in nums:
        if num == 'Z':
            total -= prev
        else:
            total += int(num)
            prev = int(num)
    
    return total