#day 8

#4. dictionary

c= {"name":"bond"}
print(type(c))
#we use {} for dictionary same as set but the differnce is key  and from the above code we can know which data type is it

# dictionary powers

# 1. mutable

m = {"name": "Dexter", "age": 20}
m["age"] = 21
print(m)
# we changed 20 into 21 because dictionary is mutable

# 2. duplicates not allowed in keys (but values can repeat)

b = {"a": 1, "b": 1}
print(b)
# here values are same, but keys are unique

# 3. ordered - dictionary does have index order but we can access through values

numbers={1:100,2:200,3:300}
print(numbers[1])

# 4. heterogeneous

d = {1: "number", "pi": 3.14, True: "boolean", 5+3j: "complex", "func": print}
print(d)
# we can store multiple data types as keys or values

#useful things

f={1:2,2:2,3:3,5:5}

f[1]=1 #updating
f[4]=4 #adding
del f[5]#deleting

print(f)

#dictionary traversing

d={1:2,2:2,3:3,5:5}

#for accessing keys
for i in d:
    print(i)

#for accessing values
for i in d:
    print(d[i])

#2.dictionary method

dictionary = {}
print(dir(dictionary))
#with this we can get all the methods

help(dictionary)
#with this we can get use of all the methods


#adeep copy and shallow copy

#deep copy - whee if we change thing in b then things in a also change

a=[1,2,3,4,5]

b=a

b[0]=100
print(a)

#shallow copy - whee if we change thing in b then things in a wont change

a=[1,2,3,4,5]

b=a.copy()

b[0]=100
print(a)

#some useful methods in dectionary

#1.clear - remove all

h={1:100,2:200,3:300,4:400,5:500}
h.clear()
print(h)

#2.copy - shallow copy

h={1:100,2:200,3:300,4:400,5:500}

p=h.copy()
print(p)

#etc