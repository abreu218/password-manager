# create a key and load key to encrypt passwords 
# if you havent created a key.... comment out lines 3-7 and use 8-11 first time you run program
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