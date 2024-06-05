def solution(arr, qrs):
    for s,e,k in qrs:
        for i in range(len(arr)):
            if s <= i <= e and i % k == 0:
                arr[i] += 1
    return arr