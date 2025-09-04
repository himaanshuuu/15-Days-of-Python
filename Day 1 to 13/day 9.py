#day 9

#errors

#syntax error

# a = 9
# print(a
      
#we got syntax error here cause we didnt closed bracket

#indentation error

# b=9
# if b==9:
# print("right")

# here we got indentation error

#zero division error

c=int(input("give us your number :- "))

print(2//c)

print("calculations are done")

#if we user gives 0 then we will get zero division error called as exception and cause of that the other code will not work 

#exception handling

#for zero error divison 

number=int(input("give us your number :- "))

try:
 print(2/number)

except ZeroDivisionError:
     print("sorry you cannot divide by zero")

print("calculations are done")


#for other error divison 

number=int(input("give us your number :- "))

try:
 print(2/number)

except Exception as error:
     print(f"sorry there is error as {error}")

else:
 print("great,there are no exceptions")

finally:
  print("i must run code no matter what")

print("alright,all calculations are done")

#raise

age=int(input("tell your age:- "))

try:
  
  if age<10 or age>20:
      raise ValueError("your age must be between 10 and 18")
  else:
     print("welcome to the club cricket")

except Exception as error :
   print(f"an error occured as {error}")

print("the club will start soon")

#file handling

#modes 

#r mode- to read file

p = open(r'main.py')
print(p.read())

#w mode- to create file but it overwrites again and again

o= open("newfile.txt", "w")  
o.write("finally my new is here ")
o.close()

#a mode- to create and update file

o= open("new.txt", 'a')  
o.write("finally my new file is here and im appending new stuff here")
o.close()

#x mode- to create file that doesnt exist already

o= open("new.txt", 'x')  #here we will get glitch cause new.txt is already here
