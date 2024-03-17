# Lab Exercise #2: Problem No. 9
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 16, 2024

# Get user input
username = input("Enter username: ")

# Check the length of the input and prints the result
if len(username) != 6:
    print("Username must be 6 characters long.")
elif not username[:4].isalpha() or not username[4:].isdigit():
    print("The first four characters should be alpha and the fifth and sixth should be digits.")
else:
    print("You entered 6 characters.")
    print("The first four characters are alpha and the fifth and sixth are digits.")
    
