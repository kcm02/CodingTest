def solution(want, number, discount):
    hash_table = {}
    count = 0
    
    for i in range(len(want)):
        hash_table[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        discount_10d = {}
        for product in discount[i:i+10]:
            if product in hash_table:
                discount_10d[product] = discount_10d.get(product, 0) + 1
                
        if discount_10d == hash_table:
            count += 1
        
    return count