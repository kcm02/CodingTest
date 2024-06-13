def solution(cipher, code):
    return ''.join([x for i,x in enumerate(cipher) if (i+1) % code == 0])