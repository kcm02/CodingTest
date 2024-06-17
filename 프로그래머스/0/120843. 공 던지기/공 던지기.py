def solution(numbers, k):
    return numbers[(1 + (k-1)*2) % len(numbers)-1]