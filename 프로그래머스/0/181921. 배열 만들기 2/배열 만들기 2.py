def solution(l, r):
    result = []
    for i in range(l,r+1):
        for j in str(i):
            if j != "0" and j != "5":
                break
        else:
            result.append(i)
    return sorted(result) if result else [-1]