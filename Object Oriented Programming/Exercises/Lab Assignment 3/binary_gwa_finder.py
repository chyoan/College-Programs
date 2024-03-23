# Lab Assignment #3: Problem No. 2
# Programmed by: Christian Kristopher D. Dalayoan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 23, 2024

# Write a Python program that read a binary file containing the name of 20 students together with their GWA.  
# The program will output the name of the student who got the highest GWA (including the GWA).

# Import the pickle module
import pickle

# Load the students from the binary file
with open('students.bin', 'rb') as f:
    students = pickle.load(f)

# Find the student with the highest GWA
highest_gwa = min(students, key=students.get)

# Print the results
print(students)
print(f'\nThe student with the highest GWA is: {highest_gwa}, GWA: {students[highest_gwa]}')
