#!flask/bin/python
import atexit

from flask import render_template
from flask import Flask

from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)


def tick():
    print('Tick! The time is: %s' % datetime.now())


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=tick,
    trigger=IntervalTrigger(seconds=5),
    id='printing_job',
    name='Print date and time every five seconds',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/coisa')
def hello2():
    return 'Clerton'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
