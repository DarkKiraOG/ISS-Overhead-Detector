import requests
from datetime import datetime
import smtplib
import time

USER_EMAIL = "___YOUR_EMAIL_HERE____"
USER_PASSWORD = "___YOUR_PASSWORD_HERE___"
LATITUDE = 0   # Your latitude
LONGITUDE = 0  # Your longitude


def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if LATITUDE - 5 <= iss_lat <= LATITUDE + 5 and LONGITUDE - 5 <= iss_long <= LONGITUDE + 5:
        return True


def is_dark():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_is_close() and is_dark():
        with smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___") as connection:
            connection.starttls()
            connection.login(USER_EMAIL, USER_PASSWORD)
            connection.sendmail(
                from_addr=USER_EMAIL,
                to_addrs=USER_EMAIL,
                msg="Subject:ISS Alert\n\nLook outside, the International Space Station is currently passing near your location."
            )
