from extFuncs import encrypter, getLogin, create_editFile
import os



def Find() :
    
    for file in os.listdir("/home/aidanbruner/passwords") :
        print(file.replace(".txt", ""), "\n")
    
    print()
    getLogin(input("Enter filename: "))
    print()

def Edit() :
    for file in os.listdir("/home/aidanbruner/passwords") :
        print(file.replace(".txt", ""), "\n")
    
    print()

    create_editFile(input("Choose File: "), input("Enter username: "), input("Enter password: "))

def Create() :
    filename = input("Enter Filename: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    create_editFile(filename, username, password)

def Cancel() :
    quit()


while True :
    print()
    print("Choose one: Find, Edit, Create, Cancel\n")
    userFunction = input(": ")

    if "Find" == userFunction :
        Find()
    elif "Edit" == userFunction :
        Edit()
    elif "Create" == userFunction :
        Create()
    elif "Cancel" == userFunction :
        Cancel()
    else :
        "Try again"
