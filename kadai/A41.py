def new_file(file1,file2):
    s=0
    with open(file1) as f:
        x=f.read().split('\n')
        #print(x,len(x))
    with open(file2) as f:
        y=f.read().split('\n')
        #print(y,len(y))
    for i in range(0,len(y)):
        s=i*2+1
        x.insert(s,y[i])
    #print(x)
    text = "\n".join(x)
    with open("A41-3.txt", "w") as f:
        f.write(text) 
   
file1="A41-1.txt"
file2="A41-2.txt"
new_file(file1,file2)
