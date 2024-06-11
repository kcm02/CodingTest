def solution(str_list, ex):
    return ''.join([x for x in str_list if ex not in x])