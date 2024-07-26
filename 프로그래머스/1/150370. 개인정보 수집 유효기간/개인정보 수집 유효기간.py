from datetime import datetime

def solution(today, terms, privacies):
    expiry = {term[0]: int(term[2:]) for term in terms}
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d")
    
    for i, privacy in enumerate(privacies):
        exp_MM = expiry[privacy[-1]]
        YYYY, MM, DD = map(int, privacy[:-2].split("."))
        
        MM += exp_MM
        if MM > 12:
            YYYY += (MM - 1) // 12
            MM = (MM - 1) % 12 + 1
        
        DD -= 1
        if DD == 0:
            DD = 28
            MM -= 1
            if MM == 0:
                MM = 12
                YYYY -= 1
        
        date_p = datetime(YYYY, MM, DD)
        
        if date_p < today:
            answer.append(i + 1)
    
    return answer