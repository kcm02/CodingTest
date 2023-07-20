a,b = map(list,input().split())
a.reverse()
b.reverse()

astr = ''.join(a)
bstr = ''.join(b)

if int(astr) > int(bstr):
    print(int(astr))
else:
    print(int(bstr))