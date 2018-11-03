class Person():
    def __init__(self , sex , age , name):
        if type(sex) == str and type(age) == int and type(name) == str:
            self.sex=sex
            self.age=age
            self.name=name
        else:
            raise TypeError
    
    def func(self):
        print(self.sex,self.age,self.name)

person1 = Person("male",27,"kaneko")
person1.func()
