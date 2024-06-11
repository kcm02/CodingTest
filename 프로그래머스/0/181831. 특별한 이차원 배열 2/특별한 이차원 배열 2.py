def solution(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if 0 <= i and j < len(arr[i]):
                result.append(int(arr[i][j] == arr[j][i]))
    return int(0 not in result)