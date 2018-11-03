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
 
people.append(Person("man",10,"hoge hogeo"))
people.append(Person("woman",11,"hoge hogeko"))
people.append(Person("man",12,"hoge hogetaro"))
people.append(Person("man",12))
 
for person in people:
    print(person.name)

people.append(Person("man",12,11))

