data = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(data[i]):
            print(data[i][j], end='')