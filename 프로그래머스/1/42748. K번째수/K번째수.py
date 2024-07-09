def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        i,j,k = commands[i]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer