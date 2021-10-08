import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)

    global timer
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state=DISABLED)
    reset_button.config(state=NORMAL)

    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if count > 0:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        ticks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            ticks += "✔"
        tick_label.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label - title
title_label = Label(text="Timer")
title_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

# Canvas - Tomato
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

# Button - Start
start_button = Button()
start_button.config(bg="white", text="Start", font=("Arial", 12), borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)

# Button - Reset
reset_button = Button()
reset_button.config(bg="white", text="Reset", font=("Arial", 12), borderwidth=0, command=reset_timer, state=DISABLED)
reset_button.grid(row=2, column=2)

# Label - Ticks
tick_label = Label()
tick_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
tick_label.grid(row=3, column=1)

window.mainloop()
