count=0
for i in range(1,100):
 s=i%5
 k=i%7
 if s==k:
  count+=1
print(count)
