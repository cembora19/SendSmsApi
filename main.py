import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "902b59614208da7287ea055c8c6b355d"
account_sid = "xxx"
auth_token = "xxx"

lat = 41.008240  # Örnek olarak Istanbul'un koordinatlarını kullanıyoruz
lon = 28.978359
exclude = "current,minutely,hourly,daily"  # Hariç tutmak istediğiniz veri bölümleri

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False

for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="mrb",
        from_='+14155238886',
        to='whatsapp:+xxx'
                 )
    print(message.status)
# print(weather_data["hourly"][0]["weather"][0]["id"])
