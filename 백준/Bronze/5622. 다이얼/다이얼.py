dic = {'ABC':2,'DEF':3,'GHI':4,'JKL':5,'MNO':6,'PQRS':7,'TUV':8,'WXYZ':9}
word = input()
sum = 0

for i in word:
    for j in dic:
        if j.find(i) != -1:
            sum += dic[j]+1
print(sum)