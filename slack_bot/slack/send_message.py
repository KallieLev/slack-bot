import requests
import requests.exceptions


def send_message_to_channel(url, token, channel, text):
    return requests.post(url=url,
                         params={'token': token, 'channel': channel, 'text': text})


def send_message_webhook_url(webhook_url, text):
    return requests.post(url=webhook_url,
                         params={'text': text})
