from collections import Counter
def solution(array):
    counter = Counter(array)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    return -1 if len(modes) > 1 else modes[0]