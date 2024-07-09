def solution(s, n):
    answer = ""
    for char in s:
        if char == " ":
            answer += " "
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer += new_char
        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer += new_char
    return answer
