def solution(t, p):
    answer = []
    for i in range(len(t) - len(p) + 1):
        answer.append(t[i:i+len(p)])
    return sum(1 for n in answer if int(n) <= int(p))