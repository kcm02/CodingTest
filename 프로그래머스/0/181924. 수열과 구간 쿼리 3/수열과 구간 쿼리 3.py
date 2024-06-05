def solution(arr, qrs):
    for row in qrs: # [i,j]
        i, j = row[0], row[1]
        arr[i],arr[j] = arr[j],arr[i]
    return arr