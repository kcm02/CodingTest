def find_nth_number(n):
    count = 0
    number = 666

    while count < n:
        if '666' in str(number):
            count += 1
        if count < n:
            number += 1
    
    return number

print(find_nth_number(int(input())))