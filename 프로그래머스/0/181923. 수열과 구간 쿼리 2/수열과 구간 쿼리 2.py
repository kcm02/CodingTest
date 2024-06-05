def solution(arr, qrs):
    result = []
    for s, e, k in qrs:
        tep = []
        for i in range(len(arr)):
            if s <= i <= e and arr[i] > k:
                tep.append(arr[i])
        result.append(min(tep) if tep else -1)
    return result