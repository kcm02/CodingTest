s = input()
answer = ''

for x in s:
    if x.upper() == x:
        answer += x.lower()
    else:
        answer += x.upper()

print(answer)