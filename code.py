#Password generator

import random 
import string

#character set
uppercase_set = list(string.ascii_uppercase)
lowercase_set = list(string.ascii_lowercase)
digits_set = list(string.digits)
symbols_set = ['@','$','%','^','&','(',')']
full_char_set = uppercase_set + lowercase_set + digits_set + symbols_set

def password_generator(length):
    
    # To make sure atleast one of these following character set is present in the password, choice is used
    uppercase_select = random.choice(uppercase_set)
    lowercase_select = random.choice(lowercase_set)
    digit_select  = random.choice(digits_set)
    symbols_select  = random.choice(symbols_set)
    temp_password = lowercase_select + uppercase_select + digit_select +symbols_select

    #intial temp_password is shuffled to introduce entropy
    temp_password_array = list(temp_password)
    random.shuffle(temp_password_array)
    temp_length =  length - 4

    #the temp_password is merged with the full character set until the length is achieved
    for i in range(temp_length):
        temp_password_array.append(random.choice(full_char_set))

    #the temp_password_array is shuffled again to introduce entropy
    random.shuffle(temp_password_array)

    #the list is concatenated to a string
    password = ""

    for char in temp_password_array:
        password = password + char
  
    return password

if __name__ == "__main__":
    #Getting the user length
    length = int(input("Enter the length of the password:"))
    if length < 8:
        # According to NIST cybersecurity best practices, it is necessary to have ATLEAST 8 characters for a strong password
        length = int(input("The minimum length should be 8. Enter the length of the password:"))
    else:
        gernarated_password  = password_generator(length)
        print(gernarated_password)
