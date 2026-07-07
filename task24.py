#class person, use __init__() func to assign name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
name = input("enter your name - ")
age = int(input("enter your age - "))
p = Person(name , age)
print("your name is ", p.name) 
print("your age is ", p.age) 