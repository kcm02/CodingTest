def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        if s[:i].rfind(s[i]) != -1:
            answer.append(i-s[:i].rfind(s[i]))
        else:
            answer.append(-1)
    return answer