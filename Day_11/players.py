import json
import random

with open('E:\Python\\100-days-code-challenge\Day_11\cards.json', "r", encoding="UTF-8") as file:
    cards_list = json.load(file)

class Player_BlackJack_21():

    def __init__(self, player_hand: list = [], amount_of_cards: int = 2):
        # Assign to self object
        self.player_hand = player_hand

        # Actions to execute
        for _ in range(amount_of_cards):
            card = random.choice(cards_list)
            self.player_hand.append(card)

    def add_random_card_to_stack(self, amount_of_cards: int = 1):
        for _ in range(amount_of_cards):
            card = random.choice(cards_list)
            self.player_hand.append(card)

    def print_player_hand_cards(self):
        list_of_cards = self.player_hand

        print("Your cards :")
        for i in range(len(list_of_cards)):
            card_suit = list_of_cards[i]['suit']
            card_value = list_of_cards[i]['value']
            print(f"{card_suit} : {card_value}")

    def check_card_values(self):
        list_of_cards = self.player_hand
        values_of_cards = []

        for card in list_of_cards:
            values_of_cards.append(card['value'])

        return values_of_cards

    def return_cards_in_hand(self):
        return self.player_hand

class Computer_BlackJack_21(Player_BlackJack_21):
    def __init__(self, player_hand: list = [], amount_of_cards: int = 2):
        super().__init__(player_hand, amount_of_cards)

    def print_player_hand_cards(self):
        list_of_cards = self.player_hand

        print("Computer card :")
        for i in range(1):
            card_suit = list_of_cards[i]['suit']
            card_value = list_of_cards[i]['value']
            print(f"{card_suit} : {card_value}")
