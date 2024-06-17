def solution(i, j, k):
    return sum(str(num).count(str(k)) for num in range(i,j+1))