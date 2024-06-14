def solution(num, k):
    try:
        return list(str(num)).index(str(k)) + 1
    except:
        return -1