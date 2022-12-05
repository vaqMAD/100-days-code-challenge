from interface import Interface


def secret_auction():
    pass
    auction_participants = {}
    is_more_participants = True
    possible_choices = [Interface.yes.value, Interface.no.value]

    while is_more_participants:
        participant_name = input("What is your name ? : ")
        participant_bid = int(input("What is your bid ? : "))

        auction_participants.update({participant_name: participant_bid})

        is_next_participant = input(
            "Are there any other participant to bid? Type 'yes' for yes, or 'no' for no ")
        if is_next_participant not in possible_choices:
            raise AttributeError(f"Given value : {is_next_participant} is incorrect ! Please type 'yes' for yes, or 'no' for no ")
        elif is_next_participant in possible_choices :
            if is_next_participant == Interface.yes.value :
                continue
            elif is_next_participant == Interface.no.value : 
                for value in auction_participants:
                    value = auction_participants.values()
                value = list(value)
                winner_index = value.index(max(value))
                winner =  list(auction_participants)[winner_index]
                is_more_participants = False
        return winner

print(secret_auction())

#TODO : Return formatted string with winner, maybe return rest of the offers ? Think about format of the for loop. 