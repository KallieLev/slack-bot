from datetime import datetime, timedelta

import config
from external_libs.twitter.twitter_handler import TwitterHandler


def get_python_content_last_hour():
    th = TwitterHandler()
    tweets = {}
    last_hour = datetime.utcnow() - timedelta(hours=3)
    for user_name, user_id in config.twitter_users_id.items():
        tweets[user_name] = th.get_user_tweets_from_date(user_id, last_hour)
    print(tweets)
    return tweets
