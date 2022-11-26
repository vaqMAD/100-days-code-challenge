# This program should generate you a band name based on the name of the city you grew up in, and your pet's name
# Given the simplicity of the design, we don't use a file requirements.txt -
print("Welcome to the band name generator")


def generate_band_name(city_of_birth: str = str, pet_name: str = str):
    """This function will generate a sample band name based on requirements

    Args:
        city_of_birth (str): The value of parameter is based on imput.
        pet_name (str): The value of parameter is based on imput.

    Returns:
        str : It return the band name based on city of birth and pet name
    """
    city_of_birth = input("What is name of the city you birth at ? ")
    pet_name = input("What is your pet's name ? ")

    return f"Your band name could be : {city_of_birth} {pet_name}"


print(generate_band_name())
