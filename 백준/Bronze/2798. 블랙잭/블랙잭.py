from itertools import combinations

n, m = map(int, input().split())
comb = combinations(list(map(int, input().split())), 3)
card = sorted([sum(c) for c in comb if sum(c) <= m])

print(card[-1])