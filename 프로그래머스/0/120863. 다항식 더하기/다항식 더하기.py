def solution(polynomial):
    terms = polynomial.split(' + ')
    const = 0
    total_x = 0
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                total_x += 1
            else:
                total_x += int(term[:-1])
        else:
            const += int(term)
            
    if const == 0:
        return f"{total_x}x" if total_x != 1 else 'x'
    elif total_x == 0:
        return str(const)
    else:
        return f"{total_x}x + {const}" if total_x != 1 else f"x + {const}"