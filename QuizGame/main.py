from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("\nYou've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
