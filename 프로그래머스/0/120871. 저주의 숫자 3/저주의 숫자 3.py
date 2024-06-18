def solution(n):
    result = 0
    count = 0
    while count < n:
        result += 1
        if result % 3 == 0 or '3' in str(result):
            continue
        count += 1
    return result