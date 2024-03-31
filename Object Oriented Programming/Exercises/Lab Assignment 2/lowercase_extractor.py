# Lab Exercise #2: Problem No. 10
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 16, 2024

password = "qWerTy"
new_string = ''

for letter in password:
    if letter.islower() == True:
        new_string += letter 
        
print(new_string)
