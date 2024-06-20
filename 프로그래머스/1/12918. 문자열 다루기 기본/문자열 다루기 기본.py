def solution(s):
    return len(s) in [4,6] and not any(char.isalpha() for char in s)