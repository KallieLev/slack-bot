import tweepy as tw

from handlers.slack.send_message import send_message_to_channel


class StreamListenerToSlackChannel(tw.StreamListener):
    def __init__(self, slack_url, slack_token, slack_channel):
        super(StreamListenerToSlackChannel, self).__init__()
        # the slack channel is used in order to send the statuses to
        self.slack_url = slack_url
        self.slack_token = slack_token
        self.slack_channel = slack_channel

    def on_status(self, status):
        text = '----new tweet from me----\n\n' + status.text
        send_message_to_channel(self.slack_url, self.slack_token, self.slack_channel, text)

    def on_error(self, status_code):
        return False
