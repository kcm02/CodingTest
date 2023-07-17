list = []
set = set([])
for i in range(10):
    list.append(int(input()))
    set.add(list[i]%42)

print(len(set))