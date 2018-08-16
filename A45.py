import re
def number_count(x):
    s=0
    for m in re.finditer("[0-9]{1,4}",x):
        print(m.group())
        s+=int(m.group())
    return s
    
x="I am 20 years old and 2nd elder brother. I like football and am a fun of 99ers."
y="Cumulus Networks has helped over 1000 companies build modern, web-scale networks using our innovative, open networking technology. In fact, 34% of the Fortune 50 have already adopted Cumulus Linux."
print(number_count(y))
