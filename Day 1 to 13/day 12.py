#day 12

#2.Polymorphism

class Animal:
    def show(self):
        print("wassup")

class Human(Animal):
    def show(self):
        print("how are you")

obj=Human()
obj.show()

#duck typing

class Animal :
    def show(self):
        print("hello im output")

class Human:
    def show(self):
        print("hello im also outpu")

obj=Animal()
obj2= Human()

obj.show()
obj2.show()

#3.Encapsulations 

#1. public attributes and methods - till now every attributes and method we have created was public 

#2. proteced attributes and methods 

class Punefactory :
    _a="pune"
    
    def _show(self):
        print("hello i am pune factory")

class Bhopalfactory:
    def show2(self):
        print(super()._a)

obj= Bhopalfactory()
obj.show2()

# with _ we protect attributes and methods but still we can access them cause in python this does not work unlike other languages so public and private attributes and methods same

#3. private attributes and methods 


class Punefactory :
    __a="pune"
    
    def __show(self):
        print("hello i am pune factory")

class Bhopalfactory:
    def show2(self):
        print(super().__a)

obj= Bhopalfactory()
obj.show2()

#so with __ we can make attributes and methods private

class demo:
    def __init__(self):
        self.name= "public member"  #public
        self._age=21                #protected
        self.__salary=5000          #private

def show (self):
    print("inside the class")
    print("public:",self.name)
    print("protected", self._age)
    print("private", self.__salary)

#4. Abstraction

from abc import ABC, abstractmethod

#from here we made the rules 
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class square(abstract):
    def __init__(self,side):
       self.side= side
    
    def perimeter(self):
        print("i have created") 
#and here we applied thats why we wont get any error
    def area(self):
        print("i have created")

class circle(abstract):
    def __init__(self,radius):
        self.radius= radius

    def perimeter(self):
        print("i have created")
#and here we applied thats why we wont get any error
    def area(self):
        print("i have created")

obj= circle(7)

#Dunder methods

class Point:
    def __init__(self, x, y):   
        self.x = x
        self.y = y

    def __str__(self):        
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):   
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1)        
print(p2)        

p3 = p1 + p2      
print(p3)        

#there are lots of dunder methods like we used her init,str and add