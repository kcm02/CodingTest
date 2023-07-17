list = []
max = 0
for i in range(9):
    list.append(int(input()))
    if list[i] > max:
        max = list[i]

for i in range(9):
    if list[i] == max:
        print(max)
        print(i+1)