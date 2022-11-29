import string
import random


def password_generator():
    """This function will generate password based on given values : how many characters each type you want. 

    Returns:
        list: it returs list of randomized characters 
    """
    
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    password_lower_case_letters = int(
        input("How many lower case letters would you like in your password ? \n"))
    password_upper_case_letters = int(
        input("How many upper case letters would you like in your password ? \n"))
    password_digits = int(
        input("How many digits would you like in your password ? \n"))
    punctuation_characters = int(
        input("How many punctuation characters would you like in your password ? \n"))

    finall_password = []

    for _ in range(password_lower_case_letters):
        finall_password.append(random.choice(lower_case))

    for _ in range(password_upper_case_letters):
        finall_password.append(random.choice(upper_case))

    for _ in range(password_digits):
        finall_password.append(random.choice(digits))

    for _ in range(punctuation_characters):
        finall_password.append(random.choice(punctuation))

    random.shuffle(finall_password)

    return finall_password


print(password_generator())
