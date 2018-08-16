import re
list=[]
def filter(x):
    m=0
    for i in x:
        m=i**2
        if re.search('9$' , str(m)):
            list.append(i)
    return list
x=[1,2,3,7,8,9,13,17,37]
print(filter(x))
