from pw_generator import *
from logo import logo
from getpass import getpass
from dotenv import load_dotenv
from base64 import encode
from doctest import master
from cryptography.fernet import Fernet
import os
from keys import *
import time

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
        
# write_key()

key = load_key()
fer = Fernet(key)

def password_manager():
    # use key to encrypt/encode and decrypt/decode passwords
    

    # function to add passwords to file 
    # if file doesn't exists, this will generate one
    def add_password():
        app = input("Website or App this is for: \n").upper()
        account = input("Account name: \n")
        choice = input("Would you like a password to be generated for you? type 'Y' for yes or 'N' for no\n").lower()
        while True:
            if choice == "y":
                pswrd = scrambler()
                print(f"Your new password is {pswrd}")
                break
            elif choice == "n":
                pswrd = getpass("Password:\n")
                break
            else:
                print("Invalid Entry")
                time.sleep(.3)
                continue
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
            exit()
        
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
                print("Your Entries have been cleared! \n\n\n")
            else:
                print("Wrong Password")
                time.sleep(1)
                
        else:
            print("Invalid Selection")
            continue

def master_user():
    while True:
        print(logo)
        master_pswrd = getpass("Type 'exit' to quit the program \nEnter Master Password: \n")
        master_file_exists = os.path.exists('.env')
        if master_file_exists:
            my_file = open(".env", "r")
            my_line = my_file.readline()
            password, index = my_line.split("=")
            if master_pswrd == index:
                password_manager()
                False
            elif master_pswrd == "exit":
                exit()
            else:
                print("Incorrect Password")
                print("Try Again!")
                time.sleep(.5)
                continue
                
        elif master_file_exists == False:
            with open('.env', 'a') as m:
                m.write(f"MASTER_PW={master_pswrd}")
                password_manager()
    
        
master_user()


