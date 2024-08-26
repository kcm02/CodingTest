n = int(input())
fruits = [input().split(' ') for _ in range(n)]
money, grams = 0, 0

for i in range(n):
    if fruits[i][0] == 'A':
        apple = (int(fruits[i][1]) // 12) * (int(fruits[i][2]) // 12) * (int(fruits[i][3]) // 12)
        money += apple * 4000
        grams += 1000 + (apple * 500)
    else:
        grams += 6000

print(grams)
print(money)