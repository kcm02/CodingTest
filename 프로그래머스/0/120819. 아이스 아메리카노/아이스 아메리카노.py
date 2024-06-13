def solution(money):
    count = 0
    while money >= 5500:
        money -= 5500
        count += 1
    return [count,money]