from tkinter import Tk, Label, Canvas, Button, PhotoImage, DISABLED
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        # Main Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "italic"))
        self.score_label.grid(row=0, column=1)

        # Questions Canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images\\true.png")
        self.true_button = Button(image=true_image, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file="images\\false.png")
        self.false_button = Button(image=false_image, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.update_score()
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
        else:
            question_text = "No more questions!"
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

        self.canvas.itemconfig(self.canvas_text, text=question_text)

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def update_score(self):
        question_count = self.quiz.question_number
        score = self.quiz.score
        self.score_label.config(text=f"Score: {score} / {question_count}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
