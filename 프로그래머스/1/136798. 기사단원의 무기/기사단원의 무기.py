def cnt_div(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += (1 if i == n // i else 2)
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count = cnt_div(i)
        answer += (count if count <= limit else power)
    return answer