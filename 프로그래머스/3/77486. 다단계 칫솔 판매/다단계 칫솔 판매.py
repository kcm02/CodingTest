def pyramid(seller, amount, recommend, answer):
    for i in range(len(seller)):
        name = seller[i]
        money = amount[i] * 100
        
        while name != "-" and money >= 1:
            commission = money // 10
            answer[name] += (money - commission)
            money = commission
            name = recommend[name]

def solution(enroll, referral, seller, amount):
    recommend = {}
    answer = {}

    for i in range(len(enroll)):
        recommend[enroll[i]] = referral[i]
        answer[enroll[i]] = 0

    pyramid(seller, amount, recommend, answer)

    return [answer[name] for name in enroll]
