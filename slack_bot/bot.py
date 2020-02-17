from datetime import datetime, timedelta

import config
from handlers.twitter.stream_listener import StreamListenerToSlackChannel
from handlers.twitter.twitter_handler import TwitterHandler


class Bot:
    def __init__(self):
        self.twitter_handler = TwitterHandler()

    def new_content_from_users_id(self, users_id):
        tweets = self.twitter_handler.get_users_tweets_from_date(users_id,
                                                                 datetime.utcnow() - timedelta(hours=1))
        resp = []
        for user, user_tweets in tweets.items():
            if len(user_tweets) > 0:
                resp.append(f'----the new tweets from {user}----\n')
                resp.append('\n----------------\n'.join(user_tweets))

        return '\n'.join(resp)

    def new_content(self, text):
        if not text:
            return self.new_content_from_users_id(config.twitter_python_ids)
        try:
            return self.new_content_from_users_id(config.twitter_languages_ids[text.lower()])
        except KeyError:
            return 'sorry, this programming language is not followed by us'

    def create_my_streaming_session(self):
        stream_listener = StreamListenerToSlackChannel(config.base_url + config.send_message_endpoint,
                                                       config.slack_token,
                                                       config.slack_default_channel)
        self.twitter_handler.create_stream_from_listener(stream_listener, follow=[str(config.twitter_my_id)],
                                                         is_async=True)

    def tweet(self, text):
        if not text:
            return 'cannot tweet empty text'

        try:
            self.twitter_handler.tweet(text)
            return 'tweeted!'

        except Exception:
            return 'could not tweet the text'
