import random
from interface import Interface

guess = random.randint(1, 100)
possible_choices = [Interface.hard.value, Interface.easy.value]


def easy_mode(number_of_lifes: int = 10):
    number_of_lifes = 10
    print(
        f"You have {number_of_lifes} lifes. Try to guess random number between 1 and 100 before you lose all lifes")
    while number_of_lifes > 0:
        print(f"Current number of lifes : {number_of_lifes}")
        player_pick = int(
            input(f"Please make a guess and type your number : \n"))
        if player_pick == guess:
            print(
                f"Your pick is correct! Your number : {player_pick}, random number : {guess}")
            number_of_lifes = 0
        elif player_pick < guess:
            print(
                f"Your number {player_pick} is too low than random number. You lose life")
            number_of_lifes -= 1
            continue
        elif player_pick > guess:
            print(
                f"Your number {player_pick} is too high than random number. You lose life.")
            number_of_lifes -= 1
            continue
    print(f"You are out of lives. End of game")


def hard_mode(number_of_lifes: int = 5):
    print(
        f"You have {number_of_lifes} lifes. Try to guess random number between 1 and 100 before you lose all lifes")
    while number_of_lifes > 0:
        print(f"Current number of lifes : {number_of_lifes}")
        player_pick = int(
            input(f"Please make a guess and type your number : \n"))
        if player_pick == guess:
            print(
                f"Your pick is correct ! Your number : {player_pick}, random number : {guess}")
            number_of_lifes = 0
        elif player_pick < guess:
            print(
                f"Your number {player_pick} is too low than random number. You lose life")
            number_of_lifes -= 1
            continue
        elif player_pick > guess:
            print(
                f"Your number {player_pick} is too high than random number. You lose life.")
            number_of_lifes -= 1
            continue
    print(f"You are out of lives. End of game")


difficulty = input(
    "Chose a difficulty. Type 'easy' for easy mode, or 'hard' for hard mode : \n")
if difficulty not in possible_choices:
    raise TypeError(
        f"Given value {difficulty} is incorrect ! Type 'easy' for easy, or 'hard' for hard ")
else:
    if difficulty == Interface.hard.value:
        hard_mode()
    elif difficulty == Interface.easy.value:
        easy_mode()
