def solution(food):
    result = ""
    for i in range(1,len(food)):
        if food[i] % 2:
            result += str(i) * ((food[i]-1)//2)
        else:
            result += str(i) * (food[i]//2)
    return result + "0" + result[::-1]