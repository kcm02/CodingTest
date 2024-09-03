n = int(input())
nums = set(map(int,input().split()))

m = int(input())
checks = map(int,input().split())

for check in checks:
    print(int(check in nums))