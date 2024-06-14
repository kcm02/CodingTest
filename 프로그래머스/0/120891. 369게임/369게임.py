def solution(order):
    return len([x for x in str(order) if int(x) in (3,6,9)])