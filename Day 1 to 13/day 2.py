#day 2


name = "himanshu"
age = 17
print(name, age)

print(f"my name is {name} and my age is {age}") 
# this is formatted string

# input - we use input to get ans from user

age = int(input("what's your age bro?"))
print(age)

nickname = str(input("what's your nickname bro?"))
print(nickname)

random_number = float(input("what's your random number?"))

print(random_number)

# operators

# 1. arithmetic operators - we use them to perform arithmetic operations 

a = 5
b = 10

print(a + b) 
# for addition

print(a - b)
# for subtraction

print(a * b)
# for multiplication

print(a ** b)
# for giving power

print(a / b)
# for dividing (we will get ans in float)

print(a // b)
# we will get ans in integer

print(a % b)
# for getting remainder

# and yes python also uses BODMAS rule

# 2. assignment operators

python = "coding"  # (= is assignment operator)

# 3. compound assignment operators

e = 2
e = e + 4
print(e)

# we can use both this method

d = 2
d += 4
print(d)

# we can use it for anything like += -= *=

# 4. comparison operation - its output is always in boolean (True or False)

# comparison between the numbers

M = 23
N = 23

print(M == N)
# equal

print(M != N)
# not equal

print(M > N)
# bigger

print(M < N)
# smaller

print(M >= N)
# here M is equal or bigger

print(M <= N)
# here M is equal or smaller

# comparison between the characters

print(ord("a"))
print(ord("z"))

print("a" < "z")

# (ord value increases from a to z)

# remember we can only compare two strings or two integers, not one integer and one string

# 5. logical operator - we use this with comparison operator

print(12 > 10 and 13 > 15) 
# in logical operator AND if there is one false then whole output will be false

print(12 > 10 or 13 < 15) 
# in logical operator OR if there is one true then whole output will be true

print(not 12 > 10) 
# in logical operator NOT changes the true into false and false into true
