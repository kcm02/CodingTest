def solution(cards1, cards2, goal):
    while goal:
        if cards1 and goal[0] == cards1[0]:
            cards1.remove(cards1[0])
        elif cards2 and goal[0] == cards2[0]:
            cards2.remove(cards2[0])
        else:
            return "No"
        goal.remove(goal[0])
    return "Yes"