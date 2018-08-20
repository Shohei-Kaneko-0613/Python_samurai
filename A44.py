def center2(x):#偶数
    k=0
    L1 = sorted(x.values())
    k=len(L1)//2
    return (L1[k-1]+L1[k])//2
    
def center1(x):#奇数
    m=0
    L2 = sorted(x.values())
    m=(len(L2)/2)-0.5
    return L2[int(m)]

x={ 'aaa':10 , 'bbb':20 , 'ccc':30 , 'ddd':40 , 'eee':50 , 'fff':60}
y={ 'aaa':10 , 'bbb':20 , 'ccc':30 , 'ddd':40 , 'eee':50}
if len(x)%2==0:
    print(center2(x))
else:
    print(center1(y))
