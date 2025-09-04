#day 7

#3. sets

c= {1,2,3}
print(type(c)) 
#we use {} for sets and from the above code we can know which data type is it

#set powers
 
#1.mutable

my= {1, 2, 3}
my.add(4)
print(my)

#here we can change 3 into 10 cause set is mutable

#2. duplicates

b={11,11}
print(b)
 
#we cant save same value for multiple times in set

#3.unordered

c={9,8,0}
#print(c[-1])
# there isnt any index order in sets

#4. hetrogenous

d=(16, 12.3,16j,"lists",)
print(d)
#we can save only save some things in set like string,number and tuple not everthing

#1. set traversing

a={1,2, 4,5,9 ,3, "hey"}

for i in a :
    print(i)

#we cant to traversing in set cause there isnt any index order

#2. set methods 

#1.basic

d={1,2,3,4,5}

d.add(6) 
d.remove(2)
d.discard(3)
d.pop()

print(d)

#2. union - add both varialble

m={1,2,3,4,5}
n={4,5,6,7,8}

o= m.union(n) 
#o= m|n shortcu
print(o)

#2. intersection - finds commen between em

m={1,2,3,4,5}
n={4,5,6,7,8}

o= m.intersection(n)
#o=m&n
print(o)

# differnce - he difference() method in Python sets returns the elements that are in the first set but NOT in the other set(s).

m={1,2,3,4,5}
n={4,5,6,7,8}

o= m.difference(n)
o= n.difference(m)
#o=m-n
print(o)

#symmetric- removes common values

m={1,2,3,4,5}
n={4,5,6,7,8}

o= m.symmetric_difference(n)
#o=m^n
print(o)

#if we dont want any other extra variable and want the operation in same two variables then do this 

m={1,2,3,4,5}
n={4,5,6,7,8}

m|=n 
print(m)

#or 

n|=m
print(n)
