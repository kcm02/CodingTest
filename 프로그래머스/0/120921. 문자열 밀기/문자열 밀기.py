def solution(A, B):
    a_list = []
    for i in range(len(A)):
        a_list.append(A[len(A)-i:] + A[:len(A)-i])
    num = [i for i,x in enumerate(a_list) if x == B]
    return num[0] if num else -1