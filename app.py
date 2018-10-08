import os
import json
import datetime
import psycopg2
import yaml
from flask import Flask, render_template, redirect, session
from peewee import *
from db import *
from flask_mail import Mail, Message

mail_settings = {
    "MAIL_SERVER": 'smtp.zoho.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": os.environ['PORTFOLIO_ZOHO_NAME'],
    "MAIL_PASSWORD": os.environ['PORTFOLIO_ZOHO_PW']
}

my_path = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
from cache import *
app.secret_key=os.environ['PORTFOLIO_SECRET']
app.config.update(mail_settings)
mail = Mail(app)

def yaml_it(file):
    path = os.path.join(my_path, "data/%s" % file)
    with open(path) as stream:
        return yaml.load(stream)

@app.before_request
def _db_connect():
    pg_db.connect()

@app.teardown_request
def _db_close(exc):
    if not pg_db.is_closed():
        pg_db.close()

@app.route('/', methods=['GET'])
def home():
    pics_orig = yaml_it("pics.yaml")
    pics = json.dumps(pics_orig)
    return render_template('home.html', pics=pics, pics_orig=pics_orig)

@app.route('/about', methods=['GET'])
@cache.cached()
def about():
    return render_template('about.html')

@app.route('/apps', methods=['GET'])
@cache.cached()
def apps():
    descriptions = yaml_it("descriptions.yaml")
    return render_template('apps.html', descriptions=descriptions)

@app.route('/contact', methods=['GET', 'POST'])
@cache.cached()
def contact():
    if request.method == 'POST':
        fmt = "My name is: \n%s\n\nMy email is: \n%s\n\nMy phone number is: \n%s\n\nAnd I want to say: \n%s\n" % (
                            request.form['name'],
                            request.form['email'],
                            request.form['phone'],
                            request.form['body'])

        msg = Message(subject="You received a new portfolio message",
                                    sender=os.environ['PORTFOLIO_ZOHO_NAME'],
                                    recipients=["andynaterosenberg@gmail.com"],
                                    body=fmt)

        mail.send(msg)
        return redirect('/contact')
    else:
        return render_template('contact.html')

from blog import *
app.register_blueprint(bp, url_prefix="/blog")

if __name__ == '__main__':
    app.run()
