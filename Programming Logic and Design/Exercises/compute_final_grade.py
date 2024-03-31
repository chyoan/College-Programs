#Christian Dalayoan
#November 27, 2023
#Computing for the final grade of the student

lecture_grade = float(input("Enter your grade for the lecture: "))
laboratory_grade = float(input("Enter your grade for the laboratory: "))
                  
final_grade = (lecture_grade * 0.70) + (laboratory_grade * 0.30)

print("The final grade of the student is", final_grade)