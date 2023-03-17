## Pick up the Umbrella Reminder

## Description
In this code, the weather condition of the current day is checked and if the weather is not clear, an SMS is sent to
the user to bring an umbrella.

For this purpose, the user must first register at https://openweathermap.org/ and https://console.twilio.com/.
(no payment is required to use this cap)

The first site will provide the user with an API to receive today's weather information. (More information in 
the API document: https://openweathermap.org/api)

The second site provides a virtual number to the user so that he can send SMS or WhatsApp notifications to
others (approved numbers).
(More information in the document https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1)

After registration, the user must set the specific parameters:
- Latitude & longitude (You can search on the internet: For example the site: https://www.maps.ie/coordinates.html)
- api_key received from openweathermap;
- account_sid, auth_token and virtual number received from twilio.
- The number of the recipient of the SMS, which was previously verified on twilio.

You can run this code in the cloud, defined for that daily task, and enjoy your reminder.


## How to run
run following:
```bash
python -m venv env
. env/bin/activate
pip install -r requirements.txt
python main.py
```
