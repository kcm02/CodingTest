def solution(my_string):
    comp = ["a","e","i","o","u"]
    return ''.join([x for x in my_string if x not in comp])