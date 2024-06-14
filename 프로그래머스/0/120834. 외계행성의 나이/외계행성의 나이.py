def solution(age):
    return ''.join([chr(int(x)+97) for x in str(age)])