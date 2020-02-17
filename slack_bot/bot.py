from handlers.twitter.twitter_handler import TwitterHandler
from datetime import datetime, timedelta
from handlers.twitter.stream_listener import StreamListenerToSlackChannel
import tweepy as tw
import config


class Bot:
    def __init__(self):
        self.twitter_handler = TwitterHandler()

    def new_content(self):
        tweets = self.twitter_handler.get_users_tweets_from_date(config.twitter_users_id,
                                                                 datetime.utcnow() - timedelta(hours=1))
        resp = []
        for user, user_tweets in tweets.items():
            if len(user_tweets) > 0:
                resp.append(f'----the new tweets from {user}----\n')
                resp.append('\n----------------\n'.join(user_tweets))

        return '\n'.join(resp)

    def create_my_streaming_session(self):
        stream_listener = StreamListenerToSlackChannel(config.base_url + config.send_message_endpoint,
                                                       config.slack_token,
                                                       config.slack_default_channel)
        self.twitter_handler.create_stream_from_listener(stream_listener, follow=[str(config.twitter_my_id)],
                                                         is_async=True)
