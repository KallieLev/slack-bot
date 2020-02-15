import datetime
from slack_bot import app
from flask import jsonify


@app.route('/now', methods=['POST'])
def send_current_hour():
    return jsonify({'text': str(datetime.datetime.now())})
