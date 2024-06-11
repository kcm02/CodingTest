def solution(order):
    price = 0
    for x in order:
        if x in {"icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"}:
            price += 5000
        else:
            price += 4500
    return price