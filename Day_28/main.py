from tkinter import *
import math

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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro")
    check_mark.config(text="")

    global reps
    reps = 0 
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break")
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Set up the window object
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Set up the title text label
title_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)

# Set up the canvas objects
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Tomato
tomato_img = PhotoImage(file="Day_28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)


# Set up the start button
start_button = Button(text="Start", bg=PINK,
                      highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Set up the reset button
restart_button = Button(text="Restart", bg=PINK, highlightthickness=0, command=reset_timer)
restart_button.grid(column=2, row=2)

# Set up the check mark label
check_mark = Label(text="", fg=GREEN, bg=YELLOW,
                   highlightthickness=0, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
