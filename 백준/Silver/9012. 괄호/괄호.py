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

n = int(input())

for i in range(n):
    s = input()
    print('YES' if is_balanced(s) else 'NO')