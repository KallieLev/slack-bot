import requests
import requests.exceptions


def send_message_to_channel(url, token, channel, text):
    try:
        requests.post(url=url,
                  params={'token': token, 'channel': channel, 'text': text})
    except requests.exceptions as e:
        print(e)
