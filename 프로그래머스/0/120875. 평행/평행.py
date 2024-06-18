def gradient(a,b):
    return (b[1] - a[1]) / (b[0] - a[0])

def solution(dots):
    if gradient(dots[0],dots[1]) == gradient(dots[2],dots[3]): 
        return 1
    elif gradient(dots[0],dots[2]) == gradient(dots[1],dots[3]): 
        return 1
    elif gradient(dots[0],dots[3]) == gradient(dots[1],dots[2]): 
        return 1
    return 0