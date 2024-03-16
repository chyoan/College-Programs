# Lab Exercise #2: Problem No. 6
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 16, 2024

# Function to get 1 character input only and not a digit or special character
def get_valid_input(prompt):
    while True:
        char = input(prompt)
        if len(char) > 1 or len(char) == 0:
            print("Please input 1 character only.")
        elif not char.isalpha():
            print("Input must be a valid character.")
        else:
            return char
            
# Get user input
letter = get_valid_input("Enter a letter: ")

# Checks what case is the letter and prints the result
if letter == letter.lower():
    print("Your letter is in lower case.")
else:
    print("Your letter is in upper case.")
