import datetime
from flask import jsonify

from external_libs.twitter.get_tweets import get_python_content_last_hour
from slack_bot import app


@app.route('/now', methods=['POST'])
def send_current_hour():
    return jsonify({'text': str(datetime.datetime.now())})


@app.route('/new-content', methods=['POST'])
def new_content_of_python_pages():
    tweets = get_python_content_last_hour()
    resp = []
    for user, user_tweets in tweets.items():
        if len(user_tweets) > 0:
            resp.append(f'----the new tweets from {user}----\n')
            resp.append('\n----------------\n'.join(user_tweets))
    if not resp:
        return jsonify({'text': 'sorry no new content'})
    return jsonify({'text': '\n'.join(resp)})
