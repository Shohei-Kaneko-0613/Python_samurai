import re
def number_count(x):
    s=0
    z=0
    for m in re.finditer('\d+\.*\d*',x): #整数のみ探す
        print(m.group())
        s+=float(m.group())

    return s
    
x="I am 20 years old and 2nd elder brother. I like football and am a fun of 99ers."
y="11.1 3.5 Cumulus Networks has helped over 1000 companies build modern, web-scale networks using our innovative, open networking technology. In fact, 34% of the Fortune 50 have already adopted Cumulus Linux."
print(number_count(y))
