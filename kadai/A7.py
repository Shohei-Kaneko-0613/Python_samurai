count=0
for i in range(100,200):
 x=str(i)
 s=0
 for j in x:
  s+=int(j)
# print(s)

 if s==10:
  count+=1
print(count)

