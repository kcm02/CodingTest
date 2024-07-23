def solution(survey, choices):
    point = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    types = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for i in range(len(choices)):
        if choices[i] < 4:
            types[survey[i][0]] += point[choices[i]]
        else:
            types[survey[i][1]] += point[choices[i]]

    return ''.join(max(pair, key=types.get) for pair in pairs)