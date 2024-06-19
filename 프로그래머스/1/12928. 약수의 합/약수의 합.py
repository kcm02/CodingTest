def solution(n):
    divs = []
    for i in range(1, n+1):
        if not n % i:
            divs.append(i)
    return sum(divs)