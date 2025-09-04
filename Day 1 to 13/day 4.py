# DAY 4

#while loop

a= 1
while a <=50:
    print(a)
    a = a+1

#while loop questions

#1. seprate the each digit of the given number and print it on new line

a = int(input("give me your number"))

while a>0:
    print(a%10)
    a=a//10

#2. reverse the given number

a = int(input("give me your number"))

rev = 0

while a>0:
    rev= rev*10 + a % 10
    a=a//10
print(rev)

# check if given no. is pallindromic or not 

a = int(input("give me your number: "))

copy = a
rev = 0

while a > 0:
    rev = rev *10 + a % 10
    a = a // 10

if copy == rev:
    print("given number is pallindromic")
else:
    print("given number is not pallindromic")


#functions

#A function in Python is a defined section of code that takes an input, performs a specific task and provides an output.

def hello():                                    # we can make our function using def
    print("this is my new function hello")

hello()

# parameters and arguments

#parameter - the thing you accept is parameter
#arguments - the thing you provide to parameter is argument

def multiplication(a,b):                                   
    print(f"the multiplication of numbers is {a * b}")

multiplication(166,167)
multiplication(1089,87361)

#here a and b are called parameters.
#and 166, 167 and 1089, 87361 are arguments.

#there are 3 types of arguments 

#1. position arguments

def multiplication(a,b):                                   
    print(f"the multiplication of numbers is {a * b}")

multiplication(166,167)
multiplication(1089,87361)

#2. keyword arguments

def information(name,age):                                   
    print(f"the name is {name} and age is {age}")

information(age= 17, name = "joe")

#3. default arguments

def information(name = "dexter",age = 17):                                   
    print(f"the name is {name} and age is {age}")

information()

#question 1 

def pallindrome (a):
    rev=""
    for i in range (len(a)-1,-1,-1):
        rev= rev+ a[i]

    if rev==a:
        print(f"{a} is a pallindrome")
    else:
        print(f"{a} isnt a pallindrome")

pallindrome ("naman")
pallindrome ("suyash")

#return

def word():
    return "hello how are you"

print(word())