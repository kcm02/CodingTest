def solution(arr, qrs):
    for row in qrs:
        arr[row[0]],arr[row[1]] = arr[row[1]],arr[row[0]]
    return arr