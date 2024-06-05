def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if bool(mode): # mode가 1일 때
            if code[i] == "1":
                mode = 0
            else:
                if i%2 == 1:
                    ret += code[i]
        else: # mode가 0일 때
            if code[i] == "1":
                mode = 1
            else:
                if i%2 == 0:
                    ret += code[i]

    return ("EMPTY" if ret == '' else ret)