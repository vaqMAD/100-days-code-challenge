# This program should generate you a band name based on the name of the city you grew up in, and your pet's name
# Given the simplicity of the design, we don't use a file requirements.txt -
print("Welcome to the band name generator")


def generate_band_name(city_of_birth=str, pet_name=str):
    city_of_birth = input("What is name of the city you birth at ? ")
    pet_name = input("What is your pet's name ? ")
    band_name_dict = {
        "City": city_of_birth,
        "Name": pet_name
    }

    return band_name_dict


band_name = generate_band_name()
print(f"Your band name could be : {band_name.get('City')} {band_name.get('Name')}")
