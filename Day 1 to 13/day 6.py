#day 6

#2. tuple

c= (1,2,3)
print(type(c)) 
#we use () for tuple and from the above code we can know which data type is it

#tuple powers

#1.immutable

m= (1,2,3,4)
m[-2]=10
print(m)
#here we cant change 3 into 10 cause tuple is immutable

#2. duplicates

b=(11,11)
print(b)
#we can save same value for multiple times in tuple

#3. ordered

c=(9,8,0)
print(c[0])
print(c[-1])
print(c)
# there is index order in tuple

#4. hetrogenous

d=(16, 12.3,True, 16j,"lists", print())
print(d)

#we can save multiple things in same varialbe in tuple

#1. tuple traversing

#how to use loop in list

#first way- where we can have both values and index

numbers=(12,19,67)

for i in range(len(numbers)):
    print(numbers[i])

#second way - where we can directly have values

digit=(9,67)

for i in digit:
    print(i)

#2.tuple methods

print(dir(tuple))
#with this we can get all the methods

help(tuple)
#with this we can get use of all the methods

#there are actually only two main methods in tuple

#1. t.count
#Counts how many times a value appears in the tuple.

t = (1, 2, 2, 3)
print(t.count(2))  

#2. t.index
#Finds the first index of the given value.

t = (10, 20, 30, 20,)

print(t.index(20))       
print(t.index(20,2))    

#tuple unpacking

a,b,c = (1,2,3)
print(b)

