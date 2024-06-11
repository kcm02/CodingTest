def solution(rank, attendance):
    students = sorted([(rank[i], i) for i in range(len(rank)) if attendance[i]])
    a,b,c = students[0][1], students[1][1], students[2][1]
    return 10000 * a + 100 * b + c