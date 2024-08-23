def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        map1 = bin(arr1[i])[2:].zfill(n)
        map2 = bin(arr2[i])[2:].zfill(n)
        line = ''.join('#' if int(map1[j]) + int(map2[j]) else ' ' for j in range(n))
        result.append(line)
    return result