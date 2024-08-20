def solution(t, p):
    return sum(1 for i in range(len(t)) if i+len(p) <= len(t) and int(t[i:i+len(p)] <= p))