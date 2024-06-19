def solution(s):
    s = s.lower()
    if s.count('p') == 0 and s.count('y') == 0:
        return True
    else:
        return s.count('p') + s.count('P') == s.count('y')