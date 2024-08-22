def solution(food):
    answer = ""
    for i,x in enumerate(food):
        answer += str(i) * (x // 2)
    return answer + "0" + answer[::-1]