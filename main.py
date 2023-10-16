import requests
from twilio.rest import Client

account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"
API_KEY = "YOUR API KEY"
FROM_NUM = "YOUR TWILIO NUM"
TO_NUM = "TO NUM"
CITY = "YOUR CITY"

parameters = {
    "q": CITY,
    "appid": API_KEY
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather?",
                        params=parameters)
response.raise_for_status()
condition_code = response.json()["weather"][0]["id"]

if condition_code < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today ☔.",
        from_=FROM_NUM,
        to=TO_NUM
    )
    print(message.status)
