import time
import requests
from twilio.rest import Client

account_sid = "AC8c6e212a56ae6307a5e2d345c7b3b23d"
auth_token = "3071d536eccea43fa1036e72c7464b78"
client = Client(account_sid, auth_token)


def get_status(user_id):
    params = {
        "access_token": "f0aa074ac35127898dfe0ba3e99c8c5770111f095c48ceb83d783c25f269236052133fa78afde2fda5b1c",
        "user_ids": user_id,    
        "v": "5.92",
        "fields": "online"
    }
    url = 'https://api.vk.com/method/users.get'
    user_status = requests.post(url, params=params)
    return user_status.json()["response"][0]["online"]  # Верните статус пользователя в ВК


def sms_sender(sms_text):
    message = client.messages.create(
    to="+79158137334", 
    from_="+12057297134",
    body= sms_text)
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
