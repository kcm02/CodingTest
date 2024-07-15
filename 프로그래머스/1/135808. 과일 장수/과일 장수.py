def solution(k, m, score):
    sorted_score = sorted(score,reverse=True)
    box = [sorted_score[i:i+m] for i in range(0,len(score),m)]
    answer = 0
    
    for apple in box:
        if len(apple) < m:
            continue
        answer += (min(apple) * m)
    return answer