def solution(sizes):
    max_list, min_list = [], []
    for x,y in sizes:
        max_list.append(max(x,y))
        min_list.append(min(x,y))
    return max(max_list) * max(min_list)