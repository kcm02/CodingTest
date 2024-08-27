def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    count = [0] * len(patterns)
    
    for i, x in enumerate(answers):
        for j in range(len(patterns)):
            pattern = patterns[j]
            if x == pattern[i % len(pattern)]:
                count[j] += 1
                
    max_score = max(count)
    highest_scores = [i+1 for i, x in enumerate(count) if x == max_score]
    return highest_scores