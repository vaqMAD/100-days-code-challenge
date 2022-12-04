import string
from interface import Interface


def encode_message(message: str, letter_shift: int):
    """Encode message for given index of shift

    Args:
        message (str): message from user
        letter_shift (int): index of shift

    Raises:
        AttributeError: when character in message do not belong in alfabeth 

    Returns:
        string: it returns already encrypted string
    """
    alfabeth = list(string.ascii_lowercase)
    encoded_letters = []

    for message_letter in message:
        message_letter = message_letter.lower()
        if message_letter == " ": #Check if message letter is space if yes append it at current position
            encoded_letters.append(message_letter)
        else: 
            for position in range(len(alfabeth)):  #Position takes current index of iteration
                if message_letter == alfabeth[position]: #If Given message letter (for iteration) is equal to current alfabeth iteration
                    try: #Try to append the alfabeth letter for current position  to the encoded letters
                        shifted_index = position + letter_shift
                        endoded_shifted_letter = alfabeth[shifted_index]
                        encoded_letters.append(endoded_shifted_letter)
                    except IndexError: #In case of IndexError 
                        shifted_index = (
                            position - len(alfabeth)) + letter_shift #We reduce the current position value by the alfabeth len and we are adding shift index 
                        endoded_shifted_letter = alfabeth[shifted_index] #EG. If index of position is 26 : 26(current position index) -26(len of alfabeth) +3(shift index) -> the searching position index is  3  
                        encoded_letters.append(endoded_shifted_letter)
                elif message_letter not in alfabeth:
                    raise AttributeError(
                        f'Given character:"{message_letter}" do not belong to alfabeth')

    endcoded_message = "".join(encoded_letters)
    return endcoded_message


def decode_message(message: str, letter_shift: int):
    """Decode message for given index of shift

    Args:
        message (str): message from user
        letter_shift (int): index of shift

    Raises:
        AttributeError: when character in message do not belong in alfabeth 

    Returns:
        string: it returns already decrypted string
    """
    alfabeth = list(string.ascii_lowercase)
    decoded_letters = []

    for message_letter in message:
        message_letter = message_letter.lower()
        if message_letter == " ":
            decoded_letters.append(message_letter)
        else:
            for position in range(len(alfabeth)):
                if message_letter == alfabeth[position]:
                    try:
                        shifted_index = position - letter_shift #When we want to decode it would be enought to reduce the index position by the index of shift 
                        endoded_shifted_letter = alfabeth[shifted_index]
                        decoded_letters.append(endoded_shifted_letter)
                    except IndexError:
                        shifted_index = (
                            position - len(alfabeth)) + letter_shift #In other cases we do not need to change anything 
                        endoded_shifted_letter = alfabeth[shifted_index] #EG. If  a(index : 0). 0-26 + 3(shift index) -> searching index is -23 means - x
                        decoded_letters.append(endoded_shifted_letter)
                elif message_letter not in alfabeth:
                    raise AttributeError(
                        f'Given character:"{message_letter}" do not belong to alfabeth')

    endcoded_message = "".join(decoded_letters)
    return endcoded_message


def main_program():
    """Used to call all needed functions, ang generate needed program components

    Raises:
        ValueError: when user choice in mode_selection input is different than 2 given choices 'encrypt' or 'decrypt'

    Returns:
        string  : it retur already encoded/decoded string based on user input
    """
    possible_choices = [Interface.Decode.value, Interface.Encode.value] 

    mode_selection = input(
        "Type 'encode' to encrypt,or  type 'decode' to decrypt\n").lower() 

    if mode_selection not in possible_choices:
        raise ValueError(
            f"Given value {mode_selection} is incorrect! Please type : 'encode' to encrypt, or  type 'decode' to decrypt")
    else:
        if mode_selection == Interface.Encode.value:
            user_mesage = input("Please type your message to encode : \n")
            user_shift_index = input("Please type your shift index :\n")
            user_shift_index = int(user_shift_index)
            return encode_message(user_mesage, user_shift_index)
        elif mode_selection == Interface.Decode.value:
            user_mesage = input("Please type your message to encode : \n")
            user_shift_index = input("Please type your shift index :\n")
            user_shift_index = int(user_shift_index)
            return decode_message(user_mesage, user_shift_index)


print(f"Your answer is : '{main_program()}'")
