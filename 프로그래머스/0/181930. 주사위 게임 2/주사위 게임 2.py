def solution(a, b, c):
    answer = 0
    if a == b == c: # 모두 같다면
        answer = (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))*(pow(a,3)+pow(b,3)+pow(c,3))
    elif a != b and b != c and c != a: # 모두 다르다면
        answer = a+b+c
    else: answer = (a+b+c)*(pow(a,2)+pow(b,2)+pow(c,2))
    
    return answer