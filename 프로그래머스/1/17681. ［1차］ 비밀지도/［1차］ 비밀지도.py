def solution(n, arr1, arr2):
    return [
        ''.join('#' if (a | b) & (1 << (n - i - 1)) else ' ' for i in range(n))
        for a, b in zip(arr1, arr2)
    ]