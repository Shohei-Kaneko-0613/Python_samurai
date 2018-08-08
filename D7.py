class Person:
    def __init__(self,sex,age,name="no name"):
 
        if type(sex) == str:
            self.sex = sex
        else:
            raise TypeError
 
        if type(age) == int:
            self.age = age
        else:
            raise TypeError
 
        if type(name) == str:
            self.name = name
        else:
            raise TypeError
 
people = []
 
people.append(Person("man",4,"Choge hogeo"))
people.append(Person("woman",2,"Bhoge hogeko"))
people.append(Person("man",3,"Ahoge hogetaro"))
people.append(Person("man",1,"Zhoge"))

L=[]
for person in people:
    s=person.age,person.name
    L.append(s)
x=sorted(L)
for i in x:
    print(i[1])

