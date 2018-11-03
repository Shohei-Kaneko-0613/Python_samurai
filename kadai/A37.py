def directory_pass(x,y):
    m=0
    s=x.split("/")
    m=s[0:-y+-1]
    return str("/".join(m))+"/"

x="/aaa/bbb/ccc/"
y=2
print(directory_pass(x,y))
