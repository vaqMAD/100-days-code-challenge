import string
from interface import Interface


def encode_message(message: str, letter_shift: int):
    alfabeth = list(string.ascii_lowercase)
    encoded_letters = []

    for message_letter in message:
        message_letter = message_letter.lower()
        if message_letter == " ":
            encoded_letters.append(message_letter)
        else:
            for position in range(len(alfabeth)):
                if message_letter == alfabeth[position]:
                    try:
                        shifted_index = position + letter_shift
                        endoded_shifted_letter = alfabeth[shifted_index]
                        encoded_letters.append(endoded_shifted_letter)
                    except IndexError:
                        shifted_index = (
                            position - len(alfabeth)) + letter_shift
                        endoded_shifted_letter = alfabeth[shifted_index]
                        encoded_letters.append(endoded_shifted_letter)
                elif message_letter not in alfabeth:
                    raise AttributeError(
                        f'Given character:"{message_letter}" do not belong to alfabeth')

    endcoded_message = "".join(encoded_letters)
    return endcoded_message


def decode_message(message: str, letter_shift: int):
    alfabeth = list(string.ascii_lowercase)
    encoded_letters = []

    for message_letter in message:
        message_letter = message_letter.lower()
        if message_letter == " ":
            encoded_letters.append(message_letter)
        else:
            for position in range(len(alfabeth)):
                if message_letter == alfabeth[position]:
                    try:
                        shifted_index = position - letter_shift
                        endoded_shifted_letter = alfabeth[shifted_index]
                        encoded_letters.append(endoded_shifted_letter)
                    except IndexError:
                        shifted_index = (
                            position - len(alfabeth)) + letter_shift
                        endoded_shifted_letter = alfabeth[shifted_index]
                        encoded_letters.append(endoded_shifted_letter)
                elif message_letter not in alfabeth:
                    raise AttributeError(
                        f'Given character:"{message_letter}" do not belong to alfabeth')

    endcoded_message = "".join(encoded_letters)
    return endcoded_message


def main_program():
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
