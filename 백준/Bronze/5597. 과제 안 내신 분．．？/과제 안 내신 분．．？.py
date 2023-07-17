student = set([i for i in range(1,31)])
report = set([])

for i in range(28):
    report.add(int(input()))

a,b = map(int,student - report)
if a > b:
    print(b,a,end='\n')
else:
    print(a,b,end='\n')