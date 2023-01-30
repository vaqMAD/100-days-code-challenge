import requests
from datetime import datetime
import smtplib
import time
import credentials


my_email = credentials.my_email
my_password = credentials.my_password

MY_LAT = 52.196580  
MY_LONG = 18.436690  

main_loop = True


def is_iss_close():
    """Check is ISS close to your coordinates

    Returns:
        True: Returns true if your current Lat and Long is within +/- ISS Lat and LONG 
    """
    request = requests.get(url="http://api.open-notify.org/iss-now.json")
    request.raise_for_status()
    data = request.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    """Check is your current time is a night time 

    Returns:
        True: Returns true if your current time is between sunset and sunrise for your location coordinates
    """

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    time_now = datetime.now().hour

    request = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    request.raise_for_status()
    data = request.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now >= sunset and time_now <= sunrise:
        return True


while main_loop:
    time.sleep(60)
    if is_iss_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="vaqowski@gmail.com",
                                msg=f"Subject: Iss is close!\n\nLook up iss is close!")
