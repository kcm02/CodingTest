def solution(k, score):
    honors = []
    answer = []
    for s in score:
        if len(honors) >= k:           
            if s > min(honors):
                honors.remove(min(honors))
                honors.append(s)
        else:
            honors.append(s)
        answer.append(min(honors))
    return answer