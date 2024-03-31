#Christian Dalayoan
#November 27, 2023
#To compute for the final grade of the student and display a message whether the student passed or failed

lecture_grade = float(input("Enter your grade for the lecture: "))
laboratory_grade = float(input("Enter your grade for the laboratory: "))
                  
final_grade = (lecture_grade * 0.70) + (laboratory_grade * 0.30)

print("Your final grade is", final_grade)

if final_grade >= 75:
    print("Congratulations, you passed!")
else:
    print("I'm sorry, but you failed.")
