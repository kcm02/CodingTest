def solution(lottos, win_nums):
    grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    if_num = lottos.count(0)
    worst = 0
    for i in win_nums:
        if i in lottos:
            worst += 1
    best = 6 if worst + if_num >= 6 else worst + if_num
    return [grade[best],grade[worst]]