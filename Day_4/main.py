import random
from interface import Interface

def rps_game():
    """This function will simulate Rock, Paper, Scissors game. All game is inplemented this function

    Raises:
        ValueError: Raises when player pick is different than possible choices (Rock, Paper, Scissors)
    """

    possible_choices = [Interface.Rock.value,
                        Interface.Paper.value, Interface.Scissors.value]

    user_choice = input(
        "What do you choose? Please type : 'Rock' for Rock, 'Paper' for Paper, 'Scissors' for Scissors ").capitalize()

    computer_choice = random.choice(possible_choices)

    if user_choice not in possible_choices:
        raise ValueError(
            f"Given value {user_choice} is incorrect! Please type : 'Rock' for Rock, 'Paper' for Paper, 'Scissors' for Scissors")
    else:
        if computer_choice == user_choice:
            print(
                f"You picked : {user_choice}, computer picked : {computer_choice}. It's a draw!")
        elif user_choice == Interface.Rock.value:
            if computer_choice == Interface.Paper.value:
                print(
                    f"You picked : {user_choice}, computer picked : {computer_choice}. Computer wins!")
            elif computer_choice == Interface.Scissors.value:
                print(
                    f"You picked : {user_choice}, computer picked : {computer_choice}. You win!")

        elif user_choice == Interface.Paper.value:
            if computer_choice == Interface.Rock.value:
                print(
                    f"You picked : {user_choice}, computer picked : {computer_choice}. You win!")
            elif computer_choice == Interface.Scissors.value:
                print(
                    f"You picked : {user_choice}, computer picked : {computer_choice}. Computer wins!")

        elif user_choice == Interface.Scissors.value:
            if computer_choice == Interface.Rock.value:
                print(
                    f"You picked : {user_choice}, computer picked : {computer_choice}. Computer wins!")
            elif computer_choice == Interface.Paper.value:
                print(
                    f"You picked : {user_choice}, computer picked : {computer_choice}. You win!")


rps_game()
