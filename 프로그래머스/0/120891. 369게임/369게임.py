def solution(order):
    return sum(1 for x in str(order) if x in '369')