# DAY 3

# Conditional Statements

# Driving License Detector

age = int(input("What's your age? "))

if age >= 70:
     print("Sorry sir, you're too old for that.")

elif age >= 18:
     print("You are eligible for a driving license.")
     
else:
    print("Sorry sir, you are too young for that.")


# Anime Detector

anime = input("What's your fav anime? ").lower()

if anime in ["one piece", "naruto", "bleach"]:
  print("Damn, you like one of the Big 3.") 

elif anime in ["dr stone", "steins gate", "monster"]:
       print("I guess you're one of those who watches underrated anime.") #in cause there are multiple things

elif anime == "my hero academia":   #== cause there is single thing
    print("get out")

elif anime in ["nah", "i don't watch anime", "i dont watch anime", "no"]:
    print("Bro... grow up and start now.")

else:
    print("Nice taste... I respect it.")
 
# gender and greetings

gender = str(input("whatsyour gender?")).lower()

if gender == "male":
    print( "oh hello gentlemen")

if gender == "female":
    print( "hey pretty lady")


#loops

#1. for loop  
   
#for printing number  

#we can do this by both way 1st 
a = range(1,25,1)
for i in a :
    print(i)

#2nd when we have to print forward
for i in range(1,25,1): 
    print(i)
#when we have to print from forward we should add 1st no. then next no. of last no.

# when we have to print reverse
for i in range(25,0,-1):
    print(i)
#when we have to print from reverse we should add 1st no. then previous no. of last no.

#lets print table of 36

for table in range(36,361,36):
    print(table)

#lets ask user the no. for the table

n = int(input("which table you want?"))

for i in range(n,(n*10+1), n):
    print(i)

# for printing strings

a = "smart"
for i in range(10):
    print(a)

#this way or 
b = "i need some time"
print(len(b))

for i in range(len(b)):
     print(b[i]) 

#this way
c = "i need time machine"
for char in c:
     print(char)

# break 

for i in range(1,100):
     if i == 15:
      break
     else:
        print(i)

# continue

for i in range(1,100):
     if i == 15:
      continue
     else:
        print(i)

# break and else
 
# 1st case 

for i in range(1,100):
     if i == 15:
           print("break statement executed") 
           break      
     print(i) 

else: 
    print("break statemen is not executed")  


 # 2nd case

for i in range(1,10):
     if i == 15:
           print("break statement executed") 
           break      
     print(i) 

else: 
    print("break statemen is not executed")