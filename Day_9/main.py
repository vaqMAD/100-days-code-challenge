from interface import Interface
import os
def clear(): return os.system('cls')


def secret_auction():
    auction_participants = {}  # Dictionary with participants
    is_more_participants = True  # While true auction is pending
    possible_choices = [Interface.yes.value, Interface.no.value]

    while is_more_participants:

        participant_name = input("What is your name ? : ")
        participant_bid = int(input("What is your bid ? : "))

        # Appending participants values to a  auction_participants dict
        auction_participants.update({participant_name: participant_bid})

        is_next_participant = input(
            "Are there any other participant to bid? Type 'yes' for yes, or 'no' for no : ").lower()  # Check is next auction_participant

        if is_next_participant not in possible_choices:  # Checking is input correct with the inteface values
            raise AttributeError(
                f"Given value : {is_next_participant} is incorrect ! Please type 'yes' for yes, or 'no' for no : ")
        elif is_next_participant in possible_choices:  # If input is correct, do this
            # If there are next participants continue while loop -> append more participants to auction_participants dict
            if is_next_participant == Interface.yes.value:
                clear()
                continue
            # If there aren't next participants ->  we are looking for a winner
            elif is_next_participant == Interface.no.value:
                offers = []
                for value in auction_participants.values():
                    offers.append(value)
                # Check what is the max value of the offers
                winning_amount = max(offers)
                # If winning offers are less than 2 -> there is one winner
                if offers.count(winning_amount) < 2:
                    winner = one_winner(auction_participants, winning_amount)
                    return print(f"The winners is : ", *winner, "with the ", winning_amount, " bid", sep=" ")
                else:  # If not there are more winners
                    winners = more_winners(
                        auction_participants, winning_amount)
                    return print(f"The winners is : ", *winners, "with the ", winning_amount, " bid", sep=" ")


def one_winner(auction_participants: dict, winning_amount: float):
    """Pick one winner for the  secret_auction function purposes

    Args:
        auction_participants (dict): Current participants dict - with the name of participant and value of his offer 
        winning_amount (int/float ): The winning amount from the participants

    Returns:
        list: return list with the one winner
    """
    auction_participants = auction_participants
    winning_amount = winning_amount

    winners = []
    for i in auction_participants:
        if auction_participants[i] == winning_amount:
            winners.append(i)
    return winners


def more_winners(auction_participants, winning_amount):
    """Pick two or more  winners for the  secret_auction function purposes

    Args:
        auction_participants (dict): Current participants dict - with the name of participant and value of his offer 
        winning_amount (int/float ): The winning amount from the participants

    Returns:
        list: return list with winners of auction
    """
    auction_participants = auction_participants
    winning_amount = winning_amount

    winners = []
    for i in auction_participants:
        if auction_participants[i] == winning_amount:
            winners.append(i)
    return winners


secret_auction()
