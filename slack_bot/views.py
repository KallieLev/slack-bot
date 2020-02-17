import datetime
from flask import jsonify, request

from slack_bot import app
from slack_bot.bot import Bot

bot = Bot()
bot.create_my_streaming_session()


@app.route('/now', methods=['POST'])
def send_current_hour():
    return jsonify({'text': str(datetime.datetime.now())})


@app.route('/new-content', methods=['POST'])
def new_content_of_python_pages():
    text = request.form['text']
    resp = bot.new_content(text)
    if not resp:
        return jsonify({'text': 'sorry no new content'})
    return jsonify({'text': resp})


@app.route('/tweet', methods=['POST'])
def tweet():
    text = request.form['text']
    resp = bot.tweet(text)
    return jsonify({'text': resp})
