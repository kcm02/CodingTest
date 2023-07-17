student = set([])
report = set([])

for i in range(30):
    student.add(i+1)

for i in range(28):
    report.add(int(input()))

a,b = map(int,student - report)
if a > b:
    print(b)
    print(a)
else:
    print(a)
    print(b)