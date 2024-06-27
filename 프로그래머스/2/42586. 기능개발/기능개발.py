import math

def solution(progresses, speeds):
    n = len(progresses)
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    count = 0
    max_day = days_left[0]
    answer = []
    
    for i in range(n):
        if days_left[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = days_left[i]
            count = 1
            
    answer.append(count)
    return answer