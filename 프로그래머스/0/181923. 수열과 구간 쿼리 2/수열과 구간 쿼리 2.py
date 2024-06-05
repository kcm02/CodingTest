def solution(arr, qrs):
    result = []
    for s, e, k in qrs:
        l = []
        for i in range(len(arr)):
            if s <= i <= e and arr[i] > k:
                l.append(arr[i])
        if l:
            result.append(min(l))
        else:
            result.append(-1)
    return result