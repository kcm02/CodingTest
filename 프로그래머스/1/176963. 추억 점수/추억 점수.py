def solution(name, yearning, photo):
    missing_score = {n: y for n, y in zip(name, yearning)}
    result = []
    
    for row in photo:
        num = 0
        for person in row:
            if person in missing_score:
                num += missing_score[person]
        result.append(num)
    
    return result