import datetime
from flask import Flask
from flask_apscheduler import APScheduler

import config
from handlers.slack.send_message import send_message_to_channel

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.add_job(id='send current time',
                  func=lambda: send_message_to_channel(config.base_url + config.send_message_endpoint,
                                                       config.slack_token,
                                                       config.slack_default_channel,
                                                       str(datetime.datetime.now())),
                  trigger='interval', hours=config.hours_interval_of_now)
scheduler.start()

import slack_bot.views

app.run(host='0.0.0.0', port=5000)
