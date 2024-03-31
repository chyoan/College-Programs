# Program to compute the grade of the student and display a message whether the student passed or failed and their final grade.
# December 8, 2023
# Christian Kristopher D. Dalayoan

#loop function that repeatedly asks the user for input until they provide a valid number within a specified range.
def get_input(valid_prompt, min_value, max_value):
    while True:
        try:
            value = float(input(valid_prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print("Please enter a value between " + str(min_value) + " and " + str(max_value) + ".")
        except ValueError:
            print("Invalid input.")
            
# For the grades of student in lecture
quiz_grade_lec = get_input("Enter your quiz grade in lecture: ", 0, 100)*.25
assignmentoractivity_grade_lec = get_input("Enter your assignment/activity grade in lecture: ", 0, 100)*.15
project_grade_lec = get_input("Enter your project grade in lecture: ", 0, 100)*.15
recitation_grade_lec = get_input("Enter your recitation grade in lecture: ", 0, 100)*.10
midtermorfinal_exam_lec = get_input("Enter your midterms/final exam grade in lecture: ", 0, 100)*.35

# Formula for calculating the grade for lecture
lecture_grade = (quiz_grade_lec + assignmentoractivity_grade_lec + project_grade_lec + recitation_grade_lec + midtermorfinal_exam_lec)

# Display the grade for lecture
print("Your grade for lecture is", lecture_grade)

# For the grades of student in laboratory
quiz_grade_lab = get_input("\nEnter your quiz grade in laboratory: ", 0, 100)*.25
assignmentoractivity_grade_lab = get_input("Enter your assignment/activity grade in laboratory: ", 0, 100)*.15
project_grade_lab = get_input("Enter your project grade in laboratory: ", 0, 100)*.15
recitation_grade_lab = get_input("Enter your recitation grade in laboratory: ", 0, 100)*.10
midtermorfinal_exam_lab = get_input("Enter your midterms/final exam grade in laboratory: ", 0, 100)*.35

# Formula for calculating the grade for laboratory
laboratory_grade = (quiz_grade_lab + assignmentoractivity_grade_lab + project_grade_lab + recitation_grade_lab + midtermorfinal_exam_lab)

# Display the grade for laboratory
print("Your grade for laboratory is", laboratory_grade)

# Formula on calculating the final grade
final_grade = round((lecture_grade*0.7) + (laboratory_grade*0.3))

# Display whether the student passed or failed and their final grade.
if final_grade >=97 and final_grade <=100:
    print("\nCongratulations, you passed!\nYour final grade is 1.00")
elif final_grade >=94 and final_grade <97:
    print("\nCongratulations, you passed!\nYour final grade is 1.25")
elif final_grade >=91 and final_grade <94:
    print("\nCongratulations, you passed!\nYour final grade is 1.50")
elif final_grade >=88 and final_grade <91:
    print("\nCongratulations, you passed!\nYour final grade is 1.75")
elif final_grade >=85 and final_grade <88:
    print("\nCongratulations, you passed!\nYour final grade is 2.00")
elif final_grade >=82 and final_grade <85:
    print("\nCongratulations, you passed!\nYour final grade is 2.25")
elif final_grade >=79 and final_grade <82:
    print("\nCongratulations, you passed!\nYour final grade is 2.50")
elif final_grade >=76 and final_grade <79:
    print("\nCongratulations, you passed!\nYour final grade is 2.75")
elif final_grade == 75:
    print("\nCongratulations, you passed!\nYour final grade is 3.00")
elif final_grade < 75 and final_grade > 0:
    print("\nSorry, you failed.\nYour final grade is 5.00")
else:
    print("\nInvalid grade.")