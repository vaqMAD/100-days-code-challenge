from players import Player_BlackJack_21, Computer_BlackJack_21
from card import ChangeCardValue, GenerateCardsValuesFromList

end_of_game = False


player = Player_BlackJack_21()
computer = Computer_BlackJack_21()

player_stack = player.return_cards_in_hand()
computer_stack = computer.return_cards_in_hand()

player_card_values = GenerateCardsValuesFromList(
    player_stack).generate_cards_objects()

computer_stack_values = GenerateCardsValuesFromList(
    computer_stack).generate_cards_objects()

print("Welcome to BlackJack 21 Game ")
print()
player.print_player_hand_cards()
print()
computer.print_player_hand_cards()


def participant_card_strength(participant_card_values: GenerateCardsValuesFromList):
    current_value = 0

    for card in participant_card_values:
        card_value = card.card_value
        current_value += card_value

    return current_value


def check_is_ace_in_stack(participant_card_values: GenerateCardsValuesFromList):
    for card in participant_card_values:
        card_value = card.card_value
        if card_value == 11 : 
            new_ace_value = input("You have ace in your stack. What do you want to do ? Change value for '1' or '11'. What value do you choose? Type '1' for 1, or '11' for 11 \n").int
            card.card_value = new_ace_value
        else:
            continue
            


player_strength = participant_card_strength(player_card_values)
computer_strength = participant_card_strength(computer_stack_values)


while player_strength < 17:
    player.add_random_card_to_stack()
    player_stack = player.return_cards_in_hand()
    player_card_values = GenerateCardsValuesFromList(
        player_stack).generate_cards_objects()
    player_strength = participant_card_strength(player_card_values)

while computer_strength < 17:
    computer.add_random_card_to_stack()
    computer_stack = computer.return_cards_in_hand()
    computer_stack_values = GenerateCardsValuesFromList(
        computer_stack).generate_cards_objects()
    computer_strength = participant_card_strength(computer_stack_values)

print(player_strength)
print(computer_strength)


#TODO : Potencial TODO : 1. End code the script file, with the all game scenarios. The rest functionality is done 