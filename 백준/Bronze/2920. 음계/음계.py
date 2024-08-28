l = list(map(int,input().split()))
ascending = sorted([i for i in range(1,9)])
descending = sorted([i for i in range(1,9)],reverse=True)

if l == ascending:
    print("ascending")
elif l == descending:
    print("descending")
else:
    print("mixed")