def solution(myString):
    return ''.join(["l" if ord(x) < ord("l") else x for x in myString])