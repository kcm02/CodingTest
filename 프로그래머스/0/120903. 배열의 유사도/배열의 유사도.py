def solution(s1, s2):
    return len([1 for i in range(min(len(s1), len(s2))) if s1[i] in s2])