def solution(d, budget):
    sorted_d = sorted(d)
    count = 0
    for i in sorted_d:
        if budget < i:
            break
        budget -= i
        count += 1
    return count