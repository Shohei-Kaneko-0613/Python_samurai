def new_line(file1):
    with open(file1) as f:
        s='\n'.join(filter(lambda x: x.strip(), f.read().split('\n')))
        y=s.split("\n")

    with open(file1,"w") as g:
        for i in y:
            g.write(i+"\n"+"\n")
    
    
file1="A42-1"
new_line(file1)

