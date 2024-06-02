# Write and test process_marks() function which is passed three parameters:
# infilename - the name of a text file containing a list of marks (one mark per student) which is to be read into the program
# outfilename - the name of the output file where the summary is to be written
# course_name - the name of the course

# The input file contains a list of marks (whole numbers), one mark per line. The function reads the list of marks from the input file,
# processes the marks by calculating the total number of marks (the number of students in the class) and the average mark, and finally,
# writes a summary to the outfile e.g., if the file, "Marks565.txt", is the file shown below:

# Marks565.txt
# 79
# 98
# 50
# 21
# 48
# 100

# the following code:
# process_marks("Marks565.txt", "Summary561.txt", "CompSci 565")

# produces the file:
# Compsci 565
# Number of students: 6
# Average mark: 66

def process_marks(infilename, outfilename, course_name):
    with open(infilename, 'r') as inf:
        f = inf.readlines()
        marks = [int(mark) for mark in f]
        total = sum(marks)
        number_of_students = len(marks)
        average = int(total / number_of_students)
    
    with open(outfilename, 'w') as out:
        out.write(f"{course_name}\nNumber of students: {number_of_students}\nAverage mark: {average}")

process_marks("Marks565.txt", "Summary561.txt", "CompSci 565")