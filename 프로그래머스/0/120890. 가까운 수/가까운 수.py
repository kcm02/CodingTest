def solution(array, n):
    return min([abs(n-i),i] for i in array)[1]