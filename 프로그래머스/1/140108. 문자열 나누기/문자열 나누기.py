def solution(s):
    answer = 0
    same=0
    diff=0
    for c in s:
        if same == diff:
            answer += 1
            x = c
        if c == x:
            same += 1
        else:
            diff += 1
    return answer