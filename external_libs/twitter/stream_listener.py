import tweepy as tw
from external_libs.slack.send_message import send_message_to_channel


class StreamListenerToSlackChannel(tw.StreamListener):
    def __init__(self, api, slack_url, slack_token, slack_channel):
        super().__init__(api)
        # the slack channel is used in order to send the statuses to
        self.slack_url = slack_url
        self.slack_token = slack_token
        self.slack_channel = slack_channel

    def on_status(self, status):
        text = 'new tweet from me!\n' + status
        send_message_to_channel(self.slack_url, self.slack_token, self.slack_channel, text)
