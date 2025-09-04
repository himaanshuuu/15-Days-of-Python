# Day 11

# OOPs – 4 Pillars
# 1. Inheritance, 2. Encapsulation, 3. Polymorphism, 4. Abstraction

#1. Inheritance types

# 1. Single Inheritance

class FactoryMumbai:                     # parent class / superclass
    a = "I am an attribute inside FactoryMumbai"

    def hello(self):
        print("Hello, I am a method inside FactoryMumbai")


class FactoryPune(FactoryMumbai):        # child class / subclass
    pass

obj1 = FactoryMumbai()
print(obj1.a)
obj1.hello()

obj2 = FactoryPune()
print(obj2.a)  
obj2.hello()    


# 2. Constructor with Inheritance

class Animal: 
    def __init__(self, name):     
        self.name = name       
    
    def show(self):               
        print(f"Hello, your name is {self.name}")


class Human(Animal):              
    def __init__(self, name, age):
        super().__init__(name)     
        self.age = age          
    
    def show(self):               
        print(f"Hello, your name is {self.name} and your age is {self.age}")


animal1 = Animal("Lion")
person1 = Human("Himanshu", 17)

animal1.show()
person1.show()


# 3. Multiple Inheritance

class Animal:
    name1 = "Lion"

class Human:
    name2 = "Harsh"

class Robot(Animal, Human):  
    name3 = "Bot"

obj = Robot()
print(obj.name1)   # from Animal
print(obj.name2)   # from Human
print(obj.name3)   # from Robot


# Example with constructors (order matters: left -> right)
class Animal:
    def __init__(self, name):
        print("Animal constructor called")

class Human:
    def __init__(self, name, age):
        print("Human constructor called")

class Robot(Human, Animal):   # Human first, then Animal
    name3 = "Bot"

obj = Robot("Robo", 10)   # only Human's constructor is called (due to order)


# 4. Multilevel Inheritance

class Factory1:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class Factory2(Factory1):
    def __init__(self, material, zips, colors):
        super().__init__(material, zips)
        self.colors = colors

class Factory3(Factory2):
    def __init__(self, material, zips, colors, pockets):
        super().__init__(material, zips, colors)
        self.pockets = pockets
