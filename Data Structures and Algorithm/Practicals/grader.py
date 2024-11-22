def grade_question(answer_key: list, student_answers: list, question_number: int):
    return answer_key[question_number] == student_answers[question_number]

def calculate_score(answer_key: list, student_answers: list):
    total_score = 0
    for i in range(len(answer_key)):
        if grade_question(answer_key, student_answers, i):
            total_score += 1
    return total_score

answer_key = ["A", "B", "C", "D"]
student_answers = ["A", "B", "D", "D"]
is_correct = grade_question(answer_key, student_answers, 2)
print(f"Is question 2 correct? {is_correct}")
total_score = calculate_score(answer_key, student_answers)
print(f"Total Score: {total_score}")



