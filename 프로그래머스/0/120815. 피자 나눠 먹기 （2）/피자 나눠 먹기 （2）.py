def solution(n):
    count = 1
    while count*6 % n != 0:
        count += 1
    return count