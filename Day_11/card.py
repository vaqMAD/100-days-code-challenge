class ChangeCardValue:
    def __init__(self, card: dict, card_value: int = 0):
        # Assign to self object
        self.card = card
        self.card_value = card_value

        # Actions to execute
        self.card_value = self.card['value']

    def change_card_value(self):
        special_cards_values = ['A', 'J', 'K', 'Q']

        if self.card_value in special_cards_values:
            if self.card_value == 'A':
                self.card_value = 11
            else:
                self.card_value = 10
        else:
            self.card_value = self.card_value


class GenerateCardsValuesFromList:
    def __init__(self, stack_of_cards: list):

        # Assign to self object
        self.stack_of_cards = stack_of_cards

    def generate_cards_objects(self):
        stack = []

        for card in self.stack_of_cards:
            stack.append(ChangeCardValue(card))
            card_index = self.stack_of_cards.index(card)
            stack[card_index].change_card_value()
        return stack
