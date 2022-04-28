
# Made by Adithya

# Importing necessary modules
import time
import random
from os import system , name
import string
from pyautogui import *

# Defining an empty list
valid_choices = [1,2,3]
# Defining an empty list
length_of_pass_1_list = []
# Defining an empty list
length_of_pass_2_list = []
# Defining an empty list
length_of_pass_3_list = []
# Defining an list which has all lowercase letters
small_letters = string.ascii_lowercase
# Defining a list with all uppercase letters
big_letters = string.ascii_uppercase
# Defining a function that clears the screen by checking which os the user has,and clearing it
def clearscreen():
    if name == 'nt':
        clean = system('cls')
    else:
        clean = system('clear')    
# Printing the choices for the user
print("1: Only numbers password")
print("2: Only letters password")
print("3: Mix of letters and numbers password")
# Asking the user to give some choice
user_choice = input("You: ")
try:
    user_choice = int(user_choice)
except:
    print("No such option available")
    print("Quitting!!")
    print("Hit the run button for code to run again")
    time.sleep(10)
    exit()
# A while loop which checks if user_choice is not in valid_choices list and asks user to give an input again
while user_choice not in valid_choices:
    # Printing "not a valid choice!!"
    print("Not a valid choice!!")
    # Printing
    print("Quitting!!")
    print("Hit the run button to run this program again")
    # Exiting program
    exit()
# An if statement which checks if user_choice == 1,and runs code
if user_choice == 1:
    # Calling the clearscreen() function,which clears the stuff in terminal
    clearscreen()  
    # Printing a statement
    print("Hi,this will generate an only numbers password for you")
    # Printing a statement
    print("How long would you like the password to be: ")
    # Asking user to enter the length of password
    length_of_pass_1 = int(input("Enter length of password in number format only: "))
    # Checks if length_of_pass_1 == 0,and prints statements
    if length_of_pass_1 == 0:
        # Prints a statement
        print("No password generated as you have entered 0")
        print("Hit the run button to run the program again")
        # Pauses the program for 10 seconds
        time.sleep(10)
        # Exiting the program
        exit()

    # If length of pass_1 < 0,then the below code runs
    if length_of_pass_1 < 0:
        # Print some statements
        print("It cannot be below 0")
        print("Quitting!!")
        print("Press the run button to run the program again")
        # Pauses the programs for 10 seconds
        time.sleep(10)
        # Exits the program
        exit()
    # This is a for loop which goes in length of password
    for i in range(length_of_pass_1):
        # Generates a random integer between range of 0,9
        random_number = random.randint(0,9)
        # converting random_number to a string
        random_number = str(random_number)
        # This append the random_number variable to length_of_pass_1_list
        length_of_pass_1_list.append(random_number)
    # Joins the list to one string        
    length_of_pass_1_list = "".join(length_of_pass_1_list)
    # Prints the password
    print("The Password is: " , length_of_pass_1_list)    



# An if statement which checks if user_choice == 2,and runs code
if user_choice == 2:
    # Calling the clearscreen() function,which clears the stuff in terminal
    clearscreen()  
    # Printing a statement
    print("Hi,this will generate an only letters password for you")
    # Printing a statement
    print("How many letters would you like the password to be: ")
    # Asking user to enter the length of password
    length_of_pass_2 = int(input("Enter length of password in number format only: "))
    # Checks if length_of_pass_1 == 0,and prints statements
    if length_of_pass_2 == 0:
        # Prints a statement
        print("No password generated as you have entered 0")
        print("Hit the run button to run the program again")
        # Pauses the program for 10 seconds
        time.sleep(10)
        # Exiting the program
        exit()

    # If length of pass_1 < 0,then the below code runs
    if length_of_pass_2 < 0:
        # Print some statements
        print("It cannot be below 0")
        print("Quitting!!")
        print("Press the run button to run the program again")
        # Pauses the programs for 10 seconds
        time.sleep(10)
        # Exits the program
        exit()
    # This is a for loop which goes in length of password
    for i in range(length_of_pass_2):
        # finds a random value of either 0 or 1
        value = random.randint(0,1)
        # If value == 0,then it runs code below it
        if value == 0:
            # Saves random.choice(small_letters) which finds a random letter of small_letters and saves it to a variable
            random_letter_small = random.choice(small_letters)
            # Appends random_letter_small to length_of_pass_2_list
            length_of_pass_2_list.append(random_letter_small)
        if value == 1:   
            # Saves random.choice(big_letters) which finds a random letter of big_letters and saves it to a variable 
            random_letter_big = random.choice(big_letters)
            # Appends random_letter_big to length_of_pass_2_list
            length_of_pass_2_list.append(random_letter_big)
    # Joins the value of list to a single value            
    length_of_pass_2_list = "".join(length_of_pass_2_list)
    # Prints the passwords
    print("The password is:" , length_of_pass_2_list)



# An if statement which checks if user_choice == 3,and runs code
if user_choice == 3:
    # Calling the clearscreen() function,which clears the stuff in terminal
    clearscreen()  
    # Printing a statement
    print("Hi,this will generate a password with numbers and passwords for you")
    # Printing a statement
    print("How many characters would you like the password to be: ")
    # Asking user to enter the length of password
    length_of_pass_3 = int(input("Enter length of password in number format only: "))
    # Checks if length_of_pass_1 == 0,and prints statements
    if length_of_pass_3 == 0:
        # Prints a statement
        print("No password generated as you have entered 0")
        print("Hit the run button to run the program again")
        # Pauses the program for 10 seconds
        time.sleep(10)
        # Exiting the program
        exit()

    # If length of pass_1 < 0,then the below code runs
    if length_of_pass_3 < 0:
        # Print some statements
        print("It cannot be below 0")
        print("Quitting!!")
        print("Press the run button to run the program again")
        # Pauses the programs for 10 seconds
        time.sleep(10)
        # Exits the program
        exit()
    # This is a for loop which goes in length of password
    for i in range(length_of_pass_3):
        # finds a random value of either 0 or 1
        value = random.randint(0,2)
        # If value == 0,then it runs code below it
        if value == 0:
            # Saves random.choice(small_letters) which finds a random letter of small_letters and saves it to a variable
            random_letter_small = random.choice(small_letters)
            random_letter_small = str(random_letter_small)
            # Appends random_letter_small to length_of_pass_2_list
            length_of_pass_3_list.append(random_letter_small)
        if value == 1:   
            # Saves random.choice(big_letters) which finds a random letter of big_letters and saves it to a variable 
            random_letter_big = random.choice(big_letters)
            random_letter_big = str(random_letter_big)
            # Appends random_letter_big to length_of_pass_2_list
            length_of_pass_3_list.append(random_letter_big)
        if value == 2:
            # Generates a random integer between 0,9
            random_number = random.randint(0,9)
            random_number = str(random_number)
            # Appends random_number to length_of_pass_3_list
            length_of_pass_3_list.append(random_number)                  
    final_password = "".join(length_of_pass_3_list)
    # Prints the passwords
    print("The password is:" , final_password)    