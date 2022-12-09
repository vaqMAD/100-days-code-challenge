import json
import random

with open('E:\Python\\100-Days-Challange-Bootcamp\Day_11\cards.json', "r", encoding="UTF-8") as file:
    cards_list = json.load(file)


def pick_random_card(cards: list = cards_list) -> dict:
    card = random.choice(cards)
    card_index = cards.index(card)
    cards.pop(card_index)

    return card


def check_card_value(cards: list) -> list:
    # for card in cards:
    # for i in card:
    # if i == 'suit':
    # suit = card[i]
    # continue
    # else:
    # card_value = card[i]
    #
    # card.update({suit: card_value})
    # card.pop('suit')
    # card.pop('value')
    # cards.append(card)
    #
    # return cards
    pass
    new_dict = {}
    new_list = []
    for card in cards:
        card_suit = card.get("suit")
        card_value = card.get("value")
        new_dict[card_suit] = card_value
        # card_suit = card.get("suit")
        # card_value = card.get("value")
        # new_dict.update({card_suit: card_value})
        # new_list.append(new_dict)
    new_list.append(new_dict)
    return new_list


x = []
card_1 = pick_random_card()
card_2 = pick_random_card()
card_3 = pick_random_card()

x.append(card_1)
x.append(card_2)
x.append(card_3)

print(check_card_value(x))


def change_special_cards_value(cards: list):

    special_cards_values = ['J', 'Q', 'K']
    ace_value = ['A']
    changed_special_values = []

    for card in cards:
        for i in card:
            if card[i] in special_cards_values:
                if card[i] in special_cards_values:
                    card.update({'value': 10})
                    changed_special_values.append(card)
                    continue
            elif card[i] in ace_value:
                if card[i] in ace_value:
                    card.update({'value': [1, 11]})
                    changed_special_values.append(card)
                    continue
        if card not in changed_special_values:
            changed_special_values.append(card)
        else:
            continue

    return changed_special_values


def participant_hand(amounts_of_cards: int) -> list:
    participant_hand = []

    for _ in range(amounts_of_cards):
        participant_hand.append(pick_random_card(cards_list))

    return participant_hand


def change_ace_card_value(card: dict):
    special_cards_values = ['A']

    for i in card:
        if card[i] in special_cards_values:
            card.update({'value': 10})
            return card


def player_hand(amounts_of_cards: int):
    # player_hand = []
    # for _ in range(amounts_of_cards):
    # player_hand.append(check_card_value(pick_random_card(cards_list)))
    #
    # return player_hand
    pass
    player_hand = participant_hand(amounts_of_cards)
    visible_player_hand = []
    for _ in range(amounts_of_cards):
        visible_player_hand.append(check_card_value())


def computers_hand(amounts_of_cards: int):
    computers_hand = []
    for _ in range(amounts_of_cards):
        computers_hand.append(check_card_value(pick_random_card(cards_list)))

    return computers_hand


print(change_special_cards_value(participant_hand(3)))
