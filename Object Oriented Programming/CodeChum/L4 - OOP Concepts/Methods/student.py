# Student Information - Python
# by CodeChum Admin

# Implement the class Student with the following public details:
# Class - Student:
# Public Properties:
# id_number (type: int): A unique identifier for the student.
# name (type: str): The name of the student.
# course (type: str): The course the student is enrolled in.
# Methods:
# __str__() -> str: Returns a string representation of the student's information in the format "{id_number} - {name} - {course}".
# validate_info() -> None: Prints the message "Student information is valid." or "Student information is not valid." indicating whether the student's information is valid. Validity criteria include:
# The name should contain only letters.
# The idNumber should be exactly 9 digits long.

class Student:
    def __init__(self, id_number: int, name: str, course: str):
        self.id_number = id_number
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.id_number} - {self.name} - {self.course}"

    def validate_info(self):
        if self.name.replace(' ', '').isalpha() and len(str(self.id_number)) == 9:
            print("Student information is valid.")
        else:
            print("Student information is not valid.")