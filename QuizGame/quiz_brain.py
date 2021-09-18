class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"\nQ.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(player_answer, question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
