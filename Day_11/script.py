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

#while not end_of_game:
    
player_hand = player.player_hand
computer_hand = computer.player_hand
player_cards = []


for x in range(len(player_hand)):
    cards = Card(player_hand[x])
    player_cards.append(cards)
    
print(player_cards[0].card_value)
        
