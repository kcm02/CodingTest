def touch_count(keymap, key):
    counts = []
    for k in keymap:
        if key in k:
            counts.append(k.index(key) + 1)
    return min(counts) if counts else -1

def solution(keymap, targets):
    result = []
    for target in targets:
        total_count = 0
        for key in target:
            count = touch_count(keymap, key)
            if count == -1:
                total_count = -1
                break
            total_count += count
        result.append(total_count)
    return result