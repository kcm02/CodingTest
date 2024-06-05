def solution(a, d, included):
    answer = 0
    seq = [i for i in range(a,a+d*len(included),d)]
    for i in range(len(included)):
        if included[i]: answer += seq[i]
    return answer