n = int(input())
answer = 0

for i in range(n):
    str_i = str(i)
    if i + sum(int(j) for j in str_i) == n:
        answer = i
        break
        
print(answer)