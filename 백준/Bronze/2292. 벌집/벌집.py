n = int(input())

layer, count = 1, 1

while n > count:
    count += 6 * layer
    layer += 1

print(layer)