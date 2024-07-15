def solution(k, score):
    honor = []
    answer = []
    
    for i in score:
        if len(honor) >= k:
            if i > min(honor):
                del honor[honor.index(min(honor))]
                honor.append(i)
        else:
            honor.append(i)
        answer.append(min(honor))
    return answer