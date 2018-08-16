def center2(x):#偶数
    k=0
    list = sorted(x.values())
    k=len(list)//2
    return (list[k-1]+list[k])//2
    
def center1(x):#奇数
    m=0
    list = sorted(x.values())
    m=(len(list)/2)-0.5
    return list[int(m)]

x={ 'aaa':10 , 'bbb':20 , 'ccc':30 , 'ddd':40 , 'eee':50 , 'fff':60}
y={ 'aaa':10 , 'bbb':20 , 'ccc':30 , 'ddd':40 , 'eee':50}
if len(x)%2==0:
    print(center2(x))
else:
    print(center1(y))
