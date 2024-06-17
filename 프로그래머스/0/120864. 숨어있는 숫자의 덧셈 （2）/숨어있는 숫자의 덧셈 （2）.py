import re

def solution(s):
    return sum(int(num) for num in re.findall(r'\d+', s))