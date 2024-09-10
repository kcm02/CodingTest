def is_balanced(s):
    dic = {"]":"[", ")":"("}
    stack = []
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic:
            if not stack or dic[char] != stack.pop():
                return False
    return not stack

while True:
    s = input()
    if s == ".":
        break
    print('yes' if is_balanced(s) else 'no')