def solution(dartResult):
    rules = {"S":1, "D":2, "T":3}
    point = []
    num = 0
    
    for i,s in enumerate(dartResult):
        if not s.isdigit():
            if dartResult[num:i]:
                point.append(int(dartResult[num:i]) ** rules[s])
            else:
                point.append(dartResult[num:i+1])
            num = i+1
            
    for j,p in enumerate(point):
        if p == "#":
            del point[j]
            point[j-1] *= (-1)
        elif p == "*":
            del point[j]
            point[j-1] *= 2
            if j-2 >= 0:
                point[j-2] *= 2
                    
    return sum(point)