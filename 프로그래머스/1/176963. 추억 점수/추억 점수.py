def solution(name, yearning, photo):
    score = {n:y for n,y in zip(name,yearning)}
    return [sum(score[j] for j in i if j in score) for i in photo]