# day 10

#oops - Object-Oriented Programming System

#3. imperative approach

a=8
b=9
print(a+b)

#2. functional approach

def addition (c,d):
    print(c+d)

addition(17,89)
addition(34,67)

#3. Object-Oriented Programming approach

#1. class

class Factory: 
    a = 7             # attributes - variable defined inside class are attribute

    def hello(self):  # methods - function defined inside class are method
        print("hello every one")


print("python is easy coding language")

print(Factory().a)   
Factory().hello()   

#2. object 

class Factory: 
    a = 7             # attributes - variable defined inside class are attribute

    def hello(self):  # methods - function defined inside class are method
        print("hello every one")

obj= Factory()

print(obj.a)
obj.hello()

#3. constructor

class factory :
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"your objects detail are {self.material} and {self.pockets} and {self.zips}")

reebok= factory("leather", 3, 2)
campus= factory("nylon", 3, 3)
adidas = factory("canvas", 2, 1)

reebok.show()

#types of attributes and methods

class animal:
    name = "lion"              # class attribute
    
    def __init__(self, age):   # instance attribute
        self.age = age

    def show(self):            # instance method
        print(f"Your animal's age is {self.age}")

    @classmethod
    def hello(cls):            # class method
        print("This is a class method. how are you?")

    @staticmethod
    def greet():               # static method
        print("This is a static method. how are you?")


#objects 

lion = animal(67)  

lion.show()        # instance method
lion.hello()       # class method (can also call with animal.hello())
lion.greet()       # static method (can also call with animal.greet())
