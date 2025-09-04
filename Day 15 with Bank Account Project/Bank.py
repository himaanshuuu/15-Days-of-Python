# Day 15 Bank Account Project 

import json
import random
import string
from pathlib import Path
 
class Bank: 
    database = 'Data.json' 
    data=[]

    try:
        if Path(database).exists():
            with open(database)as fs:
                 data=json.loads(fs.read())
        else:
            print("No existing database found. A new one will be created.")
    except Exception as error:
        print(f"An error occurred: {error}")

    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountnumber(cls):
        alpha  = random.choices(string.ascii_letters,k=2)
        num    = random.choices(string.digits,k=2)
        spchar = random.choices("!@#$%^&*()",k=2)
        id= alpha+num+spchar
        random.shuffle(id)
        return "".join(id)
    
    def createaccount(self):
        info = {
            "name"     : str(input("Enter Full Name: ")),
            "age"      : int(input("Enter Age: ")),
            "email"    : input("Enter Email Address: "),
            "pin"      : int(input("Set a 4-digit PIN: ")),
            "AccountNo": Bank.__accountnumber(),
            "balance"  : 0
        }
        
        if info['age'] < 18:
            print("You must be at least 18 years old to open an account.")

        elif len(str(info['pin'])) != 4:
            print("PIN must be exactly 4 digits.")

        else:
            print("\nAccount created successfully.\n Here are your account details:")
            for i in info:
                print(f"   {i}: {info[i]}")
            print("\n ⚠️ Please note down your Account Number and PIN for future use.\n")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney (self):
        accountnumber = input("Enter Account Number: ")
        pin           = int(input("Enter PIN: "))

        userdata = [i for i in Bank.data if i['AccountNo']== accountnumber and i['pin'] == pin]

        if userdata == False:
            print("No account found with the provided details.")

        else:
            amount = int(input("Enter amount to deposit: ₹"))
            if amount > 10000:
                print("Deposit limit exceeded. Maximum allowed deposit is ₹10,000.")
            elif amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"\nDeposit successful.\n   Account: {accountnumber}\n   Deposited: ₹{amount}\n   New Balance: ₹{userdata[0]['balance']}\n")
    
    def withdrawmoney (self):
        accountnumber = input("Enter Account Number: ")
        pin           = int(input("Enter PIN: "))

        userdata = [i for i in Bank.data if i['AccountNo']== accountnumber and i['pin'] == pin]

        if userdata == False:
            print("No account found with the provided details.")

        else:
            amount = int(input("Enter amount to withdraw: ₹"))
            if userdata[0]['balance'] < amount:
                print(f"Insufficient balance. Available Balance: ₹{userdata[0]['balance']}")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"\nWithdrawal successful.\n   Account: {accountnumber}\n   Withdrawn: ₹{amount}\n   Remaining Balance: ₹{userdata[0]['balance']}\n")

    def showdetails(self):
        accountnumber = input("Enter Account Number: ")
        pin           = int(input("Enter PIN: "))

        userdata = [i for i in Bank.data if i['AccountNo']== accountnumber and i['pin'] == pin]

        if userdata == False:
            print("No account found with the provided details.")
        else:
            print("\nAccount Details:")
            for i in userdata[0]:
                print(f"   {i}: {userdata[0][i]}")
            print()

    def updatedetails(self):
        accountnumber = input("Enter Account Number: ")
        pin           = int(input("Enter PIN: "))

        userdata = [i for i in Bank.data if i['AccountNo']== accountnumber and i['pin'] == pin]

        if userdata == False:
            print("No account found with the provided details.")

        else:
            print("\nNote: Age, Account Number, and Balance cannot be changed.")
            print("Leave a field blank if you do not wish to update it.\n")

            newdata = {
                "name" : input("Enter new name (or press Enter to skip): "),
                "email": input("Enter new email (or press Enter to skip): "),
                "pin"  : input("Enter new 4-digit PIN (or press Enter to skip): "),
            } 

            if newdata["name"]== "": newdata["name"]= userdata[0]['name']
            if newdata["email"]== "": newdata["email"]= userdata[0]['email']
            if newdata["pin"]=="": newdata["pin"]= userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['AccountNo'] = userdata[0]['AccountNo']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str: newdata['pin']= int(newdata['pin'])

            for i in newdata:
                if newdata[i] != userdata[0][i]:
                    userdata[0][i]= newdata[i]   

            Bank.__update()
            print("\nDetails updated successfully.\n")

    def deletaccount(self):
        accountnumber = input("Enter Account Number: ")
        pin           = int(input("Enter PIN: "))

        userdata = [i for i in Bank.data if i['AccountNo']== accountnumber and i['pin'] == pin]

        if userdata == False:
            print("No account found with the provided details.")
        else:
            check = input("Are you sure you want to delete this account? (yes/no): ").lower()
            if check == "no":
                print("Account deletion cancelled.")
            else:
                index= Bank.data.index(userdata [0])
                Bank.data.pop(index)
                print("\nAccount deleted successfully.\n")
                Bank.__update()    
            
user = Bank()


print("WELCOME TO PYTHON BANK\n")
print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Show Account Details")
print("5. Update Account Details")
print("6. Delete Account\n")


check = int(input("Enter your choice: "))

if check == 1: user.createaccount()
if check == 2: user.depositmoney()
if check == 3: user.withdrawmoney()
if check == 4: user.showdetails()
if check == 5: user.updatedetails()
if check == 6: user.deletaccount()