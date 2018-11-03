def new_line(file1):
    with open(file1) as f:
        s=filter(lambda x: x.strip(), f.read().split('\n'))
        print(s)
        print(type(s))
        #y=s.split("\n")
        #print(y)
        for j in s:
            print(j)

    with open(file1,"w") as g:
        for i in s:
            g.write(i+"\n"+"\n")
   
    
file1="A42-1"
new_line(file1)
