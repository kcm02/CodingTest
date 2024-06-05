str = input()

for s in str:
    if ord(s) < 97:
        print(chr(ord(s) + 32),end='')
    else:
        print(chr(ord(s) - 32),end='')

    
