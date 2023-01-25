from tkinter import *
import pandas
import random

"""
Project is not OOP oriented in course - it has to have access to global variables inside body of functions, otherwise it would be impossible to call function properly
"""

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- FLASHCARDS SETUP ------------------------------- #

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("Day_31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day_31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    """
    Pick next flashcard from the data - show word in French
    """
    global current_card, window_timer

    window.after_cancel(window_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(current_image, image=card_front_img)
    window_timer = window.after(3000, func=flip_card)


def flip_card():
    """
    Flip current flashcard to other side - English meaning
    """
    canvas.itemconfig(current_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def known_card():
    """
    If user known word from flashcard
    """
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day_31/data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# Set up the window object
window = Tk()
window.title("Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="Day_31/images/card_front.png")
card_back_img = PhotoImage(file="Day_31/images/card_back.png")
current_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Courier", 40, "bold"))
card_word = canvas.create_text(
    400, 263, text="", font=("Courier", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="Day_31/images/wrong.png")
unkown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unkown_button.grid(row=1, column=0)

check_image = PhotoImage(file="Day_31/images/right.png")
known_button = Button(image=check_image, highlightthickness=0,
                      command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
