def solution(s):
    return ''.join(sorted(x for x in s if s.count(x) == 1))