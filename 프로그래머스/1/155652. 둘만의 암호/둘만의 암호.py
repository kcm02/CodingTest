def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97,123) if not chr(i) in skip]
    answer = ""
    for c in s:
        new_index = (alphabet.index(c) + index) % len(alphabet)
        answer += alphabet[new_index]
    return answer