s = "aaa bbb ccc aaa bbb xxx yyy aaa zzz aaa abc xyz"
s.split()
d={}
x=0
for i in s.split():
    d.update(zip(i,x++))
print(d)
