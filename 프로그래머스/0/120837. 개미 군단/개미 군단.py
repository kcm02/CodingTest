def solution(hp):
    jant, bant, nant = 5, 3, 1
    count = 0
    
    count += hp // jant
    hp %= jant
    
    count += hp // bant
    hp %= bant
    
    count += hp
    
    return count