#day 5

#data structure 

#there are 4 data structures

#1. list

c= [1,2,3]
print(type(c))
#we use [] for list and from the above code we can know which data type is it

#list powers

#1. mutable

m= [1,2,3,4]
m[-2]=10
print(m)
#here we changes 3 into 10 cause list is mutable
#the core differnce betweeen list and strings is that we can change things after in list

#2. duplicates

b=[11,11]
print(b)
#we can save same value for multiple times 

#3. ordered

c=[9,8,0]
print(c[0])
print(c[-1])
# there is index order cause set is ordered

#4. hetrogenous

d=[16, 12.3,True, 16j,"lists", print()]
print(d)
#we can save multiple things in same varialbe cause set is hetrogenous

#1.list traversing

#how to use loop in list

#first way- where we can have both values and index

numbers=[12,19,67]

for i in range(len(numbers)):
    print(numbers[i])

#second way - where we can directly have values

digit=[9,67]

for i in digit:
    print(i)


#2.list method

print(dir(list))
#with this we can get all the methods

help(list)
#with this we can get use of all the methods

#some main and useful methods of list

#1. append() – Add one item at the end

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits) 

#2. extend() – Add multiple items at once

fruits = ["apple", "banana"]
fruits.extend(["cherry", "mango"])
print(fruits)

#3. insert() – Add at a specific position

fruits = ["apple", "banana"]
fruits.insert(1, "orange")  
print(fruits)

#4. remove() – Remove a specific value

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits) 

#5. pop() – Remove by position (and get the value)

fruits = ["apple", "banana", "cherry"]
removed = fruits.pop(1)
print(fruits)   
print(removed)  

#6. clear() – Remove all items

fruits = ["apple", "banana"]
fruits.clear()
print(fruits) 

#7. index() – Find the position of a value

fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  

# 8. count() – Count how many times an item appears

nums = [1, 2, 2, 3, 2]
print(nums.count(2))

#9. sort() – Sort the list in ascending order

nums = [3, 1, 4, 2]
nums.sort()
print(nums) 

#10. reverse() – Reverse the list order

nums = [1, 2, 3]
nums.reverse()
print(nums)

#11. copy() – Make a copy of a list

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
print(b) 

#questions

#1. sort out postitive and negative numbers
numbers = [3, -1, 5, -9, 0, 7]

print("These are the positive numbers from numbers:")
for i in numbers:
    if i >= 0:
        print(i)

print("These are the negative numbers from numbers:")
for i in numbers:
    if i < 0:
        print(i)

#2.firts get sum of number then mean of em

#this way

B=[19,78,67,15,-16]

sum=0

for i in B:
    sum=sum+i

print(sum)
print(sum/len(B))

#or this way

B = [19, 78, 67, 15, -16]
print(sum(B) / len(B))

#3. get the largest number and its index

k=[189,56,974,12808,10838747,18378476]

largest= k[0]
index=0


for i in range(len(k)):
    if k[i]>largest:
        largest=k[i]
        index= i

print(f"your largest number is {largest} at index{index}")

#4. check if the list is sorted or not

#case 1

G=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(G)-1):
    if G[i]<G[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")

#case 2

G=[10,9,8,7,6,5,4,3,2,1]

for i in range(len(G)-1):
    if G[i]<G[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")
