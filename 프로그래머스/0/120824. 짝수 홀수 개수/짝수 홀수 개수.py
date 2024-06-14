def solution(num_list):
    odd = [x for x in num_list if x%2]
    even = [x for x in num_list if not x%2]
    return [len(even),len(odd)]