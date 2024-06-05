def solution(l, r):
    result = []
    for i in range(l, r + 1):
        if all(c in {'0', '5'} for c in str(i)):
            result.append(i)
    return result if result else [-1]