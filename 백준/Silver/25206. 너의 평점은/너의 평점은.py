dic = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
total = 0
credit = 0

for i in range(20):
    obj_name,obj_credit,obj_grade = input().split()
    if obj_grade == 'P':
        continue
    total += float(obj_credit)*float(dic[obj_grade])
    credit += float(obj_credit)
print(total/credit)