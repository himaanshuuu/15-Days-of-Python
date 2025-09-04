 # Day 14 - File Handling Project

from pathlib import Path
import os

def readfilelandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1}: {item}")

def createfile():
    try:
        name = input("Please enter the file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter the content you want to write in this file: ")
                fs.write(data)
            print("File created successfully.")
        else:
            print("This file already exists.")
    except Exception as error:
        print(f"An error occurred: {error}")

def readfile():
    try:
        name = input("Please enter the file name you want to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("File read successfully.")
        else:
            print("The file does not exist.")
    except Exception as error:
        print(f"An error occurred: {error}")

def updatefile():
    try:
        name = input("Please enter the file name you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1: Change the file name")
            print("2: Overwrite the file content")
            print("3: Append content to the file")
        
            response = int(input("Please enter your choice: "))

            if response == 1:
                name2 = input("Enter the new file name: ")
                p2 = Path(name2)
                p.rename(p2)
                print("File renamed successfully.")

            if response == 2:
                with open(p, 'w') as fs:
                    data = input("Enter the new content: ")
                    fs.write(data)
                print("File content overwritten successfully.")

            if response == 3:
                with open(p, 'a') as fs:
                    data = input("Enter the content to append: ")
                    fs.write(data)
                print("Content appended successfully.")
    except Exception as error:
        print(f"An error occurred: {error}")

def deletefile():
    try:
        name = input("Please enter the file name you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted successfully.")
        else:
            print("The file does not exist.")
    except Exception as error:
        print(f"An error occurred: {error}")

print("File Management System") 

print("1: Create File")
print("2: Read File")
print("3: Update File")
print("4: Delete File")

check = int(input("Please enter your choice (1-4): "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
