import smtplib
import pandas
from birthday import Person, Today
import random
import credentials

my_email = credentials.my_email
my_password = credentials.my_password

data = pandas.read_csv("Day_32/birthdays.csv")
persons_data = data.to_dict(orient="records")


list_of_persons = []

for person in persons_data:
    list_of_persons.append(Person(person))


today = Today()


for person in list_of_persons:
    if today.day == person.day_of_birth and today.month == person.month_of_birth:
        file_path = f"Day_32/letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path, "r") as file:
            contents = file.read()
            contents = contents.replace("[NAME]", person.name)
            contents = contents.replace("[SIGNATURE]", "Damian")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="vaqowski@gmail.com",
                                msg=f"Subject: Happy Birthday!\n\n{contents}")
