import tkinter
import pandas as pd
import random


# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
ALL_CSV_PATH = "./data/spanish_words.csv"
TO_LEARN_CSV_PATH = "./data/spanish_words_to_learn.csv"


# Read data
to_learn = {}
words_df = None

try:
    words_df = pd.read_csv(TO_LEARN_CSV_PATH)
except (FileNotFoundError, pd.errors.EmptyDataError):
    words_df = pd.read_csv(ALL_CSV_PATH)
    to_learn = words_df.to_dict(orient="records")
else:
    to_learn = words_df.to_dict(orient="records")

# Event Handlers
cur_card = {}


def on_click_right():
    global words_df
    to_learn.remove(cur_card)
    words_df = pd.DataFrame(to_learn)
    words_df.to_csv(TO_LEARN_CSV_PATH, index=False)
    next_card()


def next_card():
    right_button["state"] = "disabled"
    wrong_button["state"] = "disabled"

    global cur_card
    try:
        cur_card = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(lang_text, text="Congrats!")
        canvas.itemconfig(word_text, text="All done!")
    else:
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(lang_text, text="Spanish", fill="black")
        canvas.itemconfig(word_text, text=cur_card["Spanish"], fill="black")
        window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=cur_card["English"], fill="white")
    right_button["state"] = "active"
    wrong_button["state"] = "active"


# Main Window
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, height=1000, width=1000)

# Canvas - initialize
canvas = tkinter.Canvas(width=800, height=526)

# Flash Card
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)

lang_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Canvas - config
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button
wrong_button_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, borderwidth=0, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Right Button
right_button_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_image, borderwidth=0, highlightthickness=0, command=on_click_right)
right_button.grid(row=1, column=1)

# Start
next_card()
window.mainloop()
