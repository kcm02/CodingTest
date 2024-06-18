def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        next_number = common[-1] + diff
        return next_number
    else:
        ratio = common[1] // common[0]
        next_number = common[-1] * ratio
        return next_number