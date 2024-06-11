def solution(picture, k):
    return [''.join([char * k for char in row]) for row in picture for _ in range(k)]