def solution(lottos, win_nums):
    grade = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    if_num = lottos.count(0)
    worst = sum(1 for i in lottos if i in win_nums and i != 0)
    best = min(worst + if_num, 6)
    return [grade[best], grade[worst]]