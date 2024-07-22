def solution(X, Y):
    from collections import Counter
    
    countX = Counter(X)
    countY = Counter(Y)
    
    common_digits = []
    
    for digit in '9876543210':
        if digit in countX and digit in countY:
            common_count = min(countX[digit], countY[digit])
            common_digits.append(digit * common_count)
    
    if not common_digits:
        return "-1"
    
    result = ''.join(common_digits)

    if result[0] == '0':
        return "0"
    
    return result
