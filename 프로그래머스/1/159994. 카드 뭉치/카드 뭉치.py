from collections import deque

def solution(cards1, cards2, goal):
    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    while goal:
        if cards1 and goal[0] == cards1[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and goal[0] == cards2[0]:
            cards2.popleft()
            goal.popleft()
        else:
            return "No"
    
    return "Yes" if not goal else "No"