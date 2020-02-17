import tweepy as tw
import config
from datetime import datetime
from external_libs.twitter.stream_listener import StreamListenerToSlackChannel


class TwitterHandler:
    def __init__(self):
        self.auth = tw.OAuthHandler(config.twitter_key, config.twitter_secret_key)
        self.auth.set_access_token(config.twitter_access_token, config.twitter_access_token_secret)
        self.api = tw.API(self.auth)

    def get_user_statuses(self, user_id: int, count=20, page=1) -> list:
        return self.api.user_timeline(user_id=user_id, count=count, page=page)

    def get_user_tweets_from_date(self, user_id: int, from_date: datetime) -> list:
        tweets = []
        page = 1
        i = 0
        tmp_tweets = self.get_user_statuses(user_id)
        curr_tweet = tmp_tweets[0]
        while curr_tweet.created_at > from_date:
            tweets.append(curr_tweet)
            # if this is the last tweet in the bulk, get next bulk
            if i == len(tmp_tweets) - 1:
                page += 1
                tmp_tweets = self.get_user_statuses(user_id, page)
                i = 0
            else:
                i += 1
                curr_tweet = tmp_tweets[i]

        return [tweet.text for tweet in tweets]

    def get_users_tweets_from_date(self, users_id: dict, from_date: datetime) -> dict:
        tweets = {}
        for user_name, user_id in users_id.items():
            tweets[user_name] = self.get_user_tweets_from_date(user_id, from_date)
        return tweets

    def get_user_id_by_name(self, user_name):
        return self.api.get_user(screen_name=user_name).id

    def create_stream_from_listener(self, stream_listener, **kwargs):
        stream = tw.Stream(auth=self.auth, listener=stream_listener)
        stream.filter(**kwargs)
        return stream
