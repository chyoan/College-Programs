# Lab Exercise #2: Problem No. 5
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 16, 2024

# Get user input
name = input("Enter your name: ")

# Process the input
lower_name = name.lower()
upper_name = name.upper()
capitalized_name = name[0].upper() + name[1:].lower()

# Print the result
print("Name in lower case: " + lower_name)
print("Name in upper case: " + upper_name)
print("Name with first letter as upper and rest lower: " + capitalized_name)
