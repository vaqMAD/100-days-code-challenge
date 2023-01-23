from tkinter import *
from tkinter import messagebox
import string
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    """
    Generate random password 
    """
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    password_lower_case_letters = random.randint(4, 6)
    password_upper_case_letters = random.randint(2, 4)
    password_digits = random.randint(1, 2)
    punctuation_characters = random.randint(1, 2)

    password_list = []

    for _ in range(password_lower_case_letters):
        password_list.append(random.choice(lower_case))

    for _ in range(password_upper_case_letters):
        password_list.append(random.choice(upper_case))

    for _ in range(password_digits):
        password_list.append(random.choice(digits))

    for _ in range(punctuation_characters):
        password_list.append(random.choice(punctuation))

    random.shuffle(password_list)

    final_password = "".join(password_list)

    password_entry.insert(0, final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Save data in file after pressing save button
    """

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't any fields empty")
    else:
        is_data_correct = messagebox.askokcancel(
            title=website, message=f"These are the data entered \nEmail : {email}\nPassword : {password}\n Do you want to save chagnes?")
        if is_data_correct:
            with open('Day_29/data.txt', 'a') as f:
                f.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Set up the window object
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set up the canvas object
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Day_29\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, )

# Set up the text labels objects
# Website
website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
# E-mail
email_label = Label(text="E-mail / Username :")
email_label.grid(row=2, column=0)
# Password
password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

# Set ut the entries objects
# Website
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
# E-mail
email_entry = Entry(width=53)
email_entry.insert(0, "@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
# Password
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Set up the buttons objects
# Password
generate_password_button = Button(
    text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)
# Add
add_data_to_file_button = Button(text="Add", width=45, command=save)
add_data_to_file_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
