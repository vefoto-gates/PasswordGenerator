import random  # Importing the random module
import string  # Importing the string module

print(string.printable) # Printing all the printable characters
char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"  # Defining the character sequence
print(type(char_seq))   # Printing the type of the character sequence

print("Enter the required length of the password ranging from 8 to 16: ") # Getting the length of the password from the user
length = int(input())   # Converting the input to integer

if length >= 8 and length <= 16:  # Checking if the length is in the range
    password = ''       # Defining the password variable
    for len in range(length):     # Looping through the length
        random_char = random.choice(char_seq) # Getting a random character from the character sequence
        password += random_char   # Adding the random character to the password
        
    # print(password)   # Printing the password
    list_pass = list(password)    # Converting the password to a list
    random.shuffle(list_pass)     # Shuffling the list
    final_password = ''.join(list_pass)       # Converting the list to a string
    print(final_password)         # Printing the final password
else:
    print("Enter a suitable range")           # Printing an error message

    from password_generator import \
        PasswordGenerator  # Importing the PasswordGenerator class from the password_generator module
    pwo = PasswordGenerator()     # Creating an object of the PasswordGenerator class
    pwo.generate()                # Calling the generate method of the PasswordGenerator class
