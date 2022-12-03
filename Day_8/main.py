import string


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


print(encode_message("Nikola dupa xdd", 26))

# TODO : Decode_messsage function


def decode_message():
    pass

# TODO : main program function with intputs from user and user inteface


def main_program():
    pass
