from hangman_art import stages


def hangman_game():
    """
    This will simulate a hangman game  
    Attention : It works only when random_word is lower case
    """
    random_word = "test"
    lives = 6
    display = []  # This is what player sees - list filled with "_" characters as a letters in winnign word - this list will be updated if player will guess correc lette
    end_of_game = False

    # This loop will fill the display list
    for _ in random_word:
        display.append("_")

    list_of_player_picks = []  # This is list of all letters which player picked

    # This loop is going to execute if player has lives left, or player correct guessed winnig word
    while not end_of_game:
        player_pick = input("Pick a letter : ").lower()
        for position in range(len(random_word)):
            letter = random_word[position]
            if letter == player_pick:
                display[position] = letter

        if player_pick not in random_word:  # If letter picked by player is not in random_word -1 life, or end of game if lives == 0
            print(
                f"You guessed {player_pick}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True

        print(f"{' '.join(display)}")  # Print

        if "_" not in display:  # If display list is filled letters instead of "_" characters -> player wins
            end_of_game = True
            print("You win.")
        list_of_player_picks.append(player_pick)
        print(f"Your picks: {list_of_player_picks}")
        # Print current game stage - based on how many lives left
        print(stages[lives])


hangman_game()

# TODO: Potential TODO tasks : 1. Connect application with public API which will generate random word  2. Import random word and use it into hangman_game
