import requests


def send_message_to_channel(url, token, channel, text):
    requests.post(url=url,
                  params={'token': token, 'channel': channel, 'text': text})
