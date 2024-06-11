def solution(arr):
    max_len = max(len(arr), len(arr[0]))
    
    for row in arr:
        row += [0] * (max_len - len(row))
    
    arr += [[0] * max_len] * (max_len - len(arr))
    
    return arr