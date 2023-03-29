"""---------------------------------------- Pick up the Umbrella Reminder ----------------------------------------

In this code, the weather condition of the current day is checked and if the weather is not clear, an SMS is sent to
the user to bring an umbrella.

For this purpose, the user must first register at https://openweathermap.org/ and https://console.twilio.com/.
(no payment is required to use this cap)

The first site will provide the user with an API to receive today's weather information. (More information in the API
technical document: https://openweathermap.org/api)

The second site provides a virtual number to the user so that he can send SMS or WhatsApp notifications to
others (approved numbers).
(More information in the technical document https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1)

After registration, the user must set the specific parameters:
- Latitude & longitude (You can search on the internet: For example the site: https://www.maps.ie/coordinates.html)
- api_key received from openweathermap;
- account_sid, auth_token and virtual number received from twilio.
- The number of the recipient of the SMS, which was previously verified on twilio.

"""

# ---------------------------------------- Add Required Library ----------------------------------------

import os
import requests
from twilio.rest import Client
from random import choice

# ---------------------------------------- Specific Parameters Definition ----------------------------------------

my_lat = "MY_LAT"
my_long = "MY_LONG"
api_key = "API_KEY"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"
sender = "SENDER"
receiver = "RECEIVER"

# ---------------------------------------- Weather API call ----------------------------------------

user_agents = [
  "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
  "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
  ]
random_user_agent = random.choice(user_agents)
headers = {
    'User-Agent': random_user_agent
}

parameters = {
    "lat": os.getenv(my_lat),
    "lon": os.getenv(my_long),
    "appid": os.getenv(api_key),
    "exclude": "current,hourly,daily"
}

weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather", headers=headers, params=parameters)

# ---------------------------------------- Checking for Errors in api calls ----------------------------------------

weather_data.raise_for_status()

# ---------------------------------------- Data to Json Conversion ----------------------------------------

data = weather_data.json()

# ---------------------------------------- Required data Selection ----------------------------------------

weather_condition = data["weather"][0]["id"]

# ---------------------------------------- Need to Inform Assessment ----------------------------------------

need_umbrella = False

if weather_condition > 700:
    need_umbrella = True
    client = Client(os.getenv(account_sid), os.getenv(auth_token))
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_=os.getenv(sender),
        to=os.getenv(receiver)
    )

    print(message.status)
