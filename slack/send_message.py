import requests
import requests.exceptions


def send_message_to_channel(url, token, channel, text):
    return requests.post(url=url,
                         params={'token': token, 'channel': channel, 'text': text})
