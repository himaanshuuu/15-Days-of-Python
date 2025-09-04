#day 13

# advance stuff

#1. decorater

class Animal:
    @property             #with this decorater we dont need to use () in obj.show
    def show(self):
        print("wassup")

obj= Animal()
obj.show

#decorater and wrapper

def decorate(function):
    def wrapper():
        print("im oldest child")
        function()
        print("im youngest child")
    return wrapper  

@decorate
def hello():
    print("im middel child")

hello()

#decorater and wrapper with paramters

def decorate(function):
    def wrapper(a,b):
        print("wait result is loading")
        function(a,b)
        print("thank you")
    return wrapper  

@decorate
def Adittion(a,b):
    print(F"your total is {a+b}")

Adittion(12,67)

#2. Args and kwargs

#Args

def Adittion(*args):
    sum=0
    for i in args:
        sum= sum + i
    print(sum)

Adittion(12,67,8347,48784,730846)

# Kwargs

def Information(**kwargs):
    print("Your information is \n\n")
    for i in kwargs:
     print(f"{i}:{kwargs[i]}")

Information(name ="Suyash", age = 21, speciality = "vfx artist")

# Args and kwargs in decorater

def decorate(function):
    def wrapper(*args,**kwargs):
        print("wait result is loading")
        function(*args,**kwargs)
        print("thank you")
    return wrapper  

@decorate
def Adittion(a,b,c):
    print(F"your total is {a+b}")

Adittion(12,67,67)

#comprehension

#without comprehension

a=19
if a%2==0:
    print("even")
else:
    print("odd")

#with comprehension

a = 8 
l= (print("even")if a%2== 0 else print("odd"))

# Lamda functions

#without lamda

def addition(a,b):
    print(a+b)

addition(12,13)

#with lamda

addition= lambda a,b : a+b
print(addition(86,23))

# map with lamda function

a = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, a)

print(list(result))

#filter with lamda

numbers= [1,2,3,4,5]
evens= filter(lambda x: x%2==0, numbers)
print(list(evens))