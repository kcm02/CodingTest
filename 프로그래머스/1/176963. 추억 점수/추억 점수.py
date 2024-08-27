def solution(name, yearning, photo):
    score = {n:y for n,y in zip(name,yearning)}
    result = []
    for persons in photo:
        count = 0
        for person in persons:
            if person not in score:
                continue
            count += score[person]
        result.append(count)
    return result