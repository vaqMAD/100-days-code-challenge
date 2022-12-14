from players import Player_BlackJack_21, Computer_BlackJack_21
from card import Card

end_of_game = False


player = Player_BlackJack_21()
computer = Computer_BlackJack_21()

print("Welcome to BlackJack 21 Game ")
print("")
player.print_player_hand_cards()
print("")
computer.print_player_hand_cards()


player_hand = player.player_hand
computer_hand = computer.player_hand
player_cards = []
computer_cards = []


def generate_participant_stack(participant_hand):
    for i in range(len(participant_hand)):
        card = Card(participant_hand[i])
        player_cards.append(card)
        
def add_card_to_stack(participant_hand, stack_of_cards):
    for i in range(len(participant_hand)):
        card = Card(participant_hand[i])
        if card.card != stack_of_cards[i].card:
            player_cards.append(card)
        else:
            continue
        
    
generate_participant_stack(player_hand)
print(player_cards)
player.add_random_card_to_stack()
player_hand = player.player_hand
add_card_to_stack(player_hand, player_cards)
print(player_cards)



def card_strenght(participant_cards: list):
    current_value = 0
    for card in participant_cards:
        card_value = card.card_value
        current_value += card_value

    return current_value


player_strenght = card_strenght(player_cards)
