import random
s=[]
def Dec_random(x):
    
    my_list=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for i in range(x):
        s.append(random.choice(my_list))
    J="".join(s)
    return "0x"+str(J)
        
a=int(input())
print(Dec_random(a))
