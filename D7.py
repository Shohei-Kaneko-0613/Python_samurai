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
people.append(Person("woman",1,"Bhoge hogeko"))
people.append(Person("man",10,"Ahoge hogetaro"))
people.append(Person("man",-1,"Zhoge"))

def name_sorted(x):
    people_sorted = sorted(people, key=lambda x:x.age)
    for i in people_sorted:
        print(i.sex,i.age,i.name)
    
name_sorted(people)
