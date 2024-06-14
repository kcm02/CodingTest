def solution(my_string):
    return sorted([int(x) for x in my_string if x.isdigit()])