def solution(string, n1, n2):
    s_list = list(string)
    s_list[n1], s_list[n2] = s_list[n2], s_list[n1]
    return ''.join(s_list)