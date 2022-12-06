from interface import Interface
import os
def clear(): return os.system('cls')


def secret_auction():
    auction_participants = {}
    is_more_participants = True
    possible_choices = [Interface.yes.value, Interface.no.value]

    while is_more_participants:
        participant_name = input("What is your name ? : ")
        participant_bid = int(input("What is your bid ? : "))

        auction_participants.update({participant_name: participant_bid})

        is_next_participant = input(
            "Are there any other participant to bid? Type 'yes' for yes, or 'no' for no : ").lower()
        if is_next_participant not in possible_choices:
            raise AttributeError(
                f"Given value : {is_next_participant} is incorrect ! Please type 'yes' for yes, or 'no' for no : ")
        elif is_next_participant in possible_choices:
            if is_next_participant == Interface.yes.value:
                clear()
                continue
            elif is_next_participant == Interface.no.value:
                offers = []
                for value in auction_participants.values():
                    offers.append(value)
                winning_amount = max(offers)
                if offers.count(winning_amount) < 2:
                    winning_amount_index = offers.index(max(offers))
                    winner = list(auction_participants)[winning_amount_index]
                    is_more_participants = False
                    return f"The winner is {winner} with the {max(offers)} bid"
                else:
                    indexes = []
                    for i in offers:
                        if i == winning_amount:
                            indexes.append(offers.index(i))
                    # for position in range(len(offers)):
                    #    index = offers[position]
                    #    for i in offers :
                    #        if i == winning_amount:
                    #            indexes.append(indexes)
                    winners = list(auction_participants)[0, 1]
                    is_more_participants = False
                    return f"The winers are {winners} with the {max(offers)} bid"


print(secret_auction())

# TODO : Fix but with the return value for two winning  participants
