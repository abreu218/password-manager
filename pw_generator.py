import random
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '-']

# letter_amount = int(input("How many letters would you like in your password?"))
# number_amount = int(input("How many numbers would you like in your password?"))
# symbol_amount = int(input("How many symbols would you like in your password?"))



password = []
def generate_password(amount, characters):
    """Amount of certain characters that you want, choose: ['upper_letters','lower_letters', 'numbers', 'symbols']""" 
    for i in range(amount):
        rand_characters = random.choice(characters)
        password.append(rand_characters)
    return password

def scrambler():
    generate_password(2,upper_letters)
    generate_password(6,lower_letters)
    generate_password(2,numbers)
    generate_password(2,symbols)
    random.shuffle(password)
    string = "".join(password)
    return string
    
    








    



    