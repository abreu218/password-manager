from logo import logo
from getpass import getpass
from dotenv import load_dotenv
from base64 import encode
from doctest import master
from cryptography.fernet import Fernet
import os
from keys import *
import time
import maskpass




def password_manager():
    # use key to encrypt/encode and decrypt/decode passwords
    key = load_key()
    fer = Fernet(key)

    # function to add passwords to file 
    # if file doesn't exists, this will generate one
    def add_password():
        app = input("Website or App this is for: \n").upper()
        account = input("Account name: \n")
        pswrd = getpass("Password: \n")
        
        with open('password.txt', 'a') as f:
            f.write(f"{app}|{account}|{fer.encrypt(pswrd.encode()).decode()} \n")
        
    # function to view current passwords in file
    def existing_password():
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                app, user, password = data.split("|")
                print(f"App: {app} User: {user} | Password:{fer.decrypt(password.encode()).decode()}")


    # main menu to add, view or exit program
    while True:
        mode = input("""Please make a selection:
                Enter "1" to add a new password.
                Enter "2" to view existing passwords.
                Enter "3" to Exit. 
                Enter "0" To Delete all Entries.\n """)
        if mode =="3": 
            break
        
        if mode == "1":
            add_password()
            print("Password entry added.")
        elif mode =="2":
            existing_password()
        elif mode =="0":
            print("Are you sure you want to clear all entries")
            confirm = getpass("Type in the Master password to confirm: \n")
            my_file = open(".env", "r")
            my_line = my_file.readline()
            password, index = my_line.split("=")
            if confirm == index:
                file = open("password.txt", "r+")
                file.truncate(0)
                file.close()
            else:
                print("Wrong Password")
                time.sleep(1)
            
            
            
        else:
            print("Invalid Selection")
            continue

def master_user():
    while True:
        print(logo)
        master_pswrd = getpass("Enter Master Password:\n")
        master_file_exists = os.path.exists('.env')
        if master_file_exists:
            my_file = open(".env", "r")
            my_line = my_file.readline()
            password, index = my_line.split("=")
            if master_pswrd == index:
                password_manager()
                False
            else:
                print("Incorrect Password")
                time.sleep(1)
                os.system('cls')
                print("program will close in: \n 3")                
                time.sleep(1)
                os.system('cls')
                print("program will close in: \n 2")
                time.sleep(1)
                os.system('cls')
                print("program will close in: \n 1")
                time.sleep(1)
                os.system('cls')
                print("Goodbye!")
                time.sleep(.5)
                break
                
        elif master_file_exists == False:
            with open('.env', 'a') as m:
                m.write(f"MASTER_PW={master_pswrd}")
                password_manager()
    
        
           

master_user()


