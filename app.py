from flask import Flask, flash, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_cors import CORS
import boto3
import requests
import socket
import json

from src import conf, obj
from src.webchecker import check_website
#import controller

#App Configuration
app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = conf.SECRET_KEY

class Webchecker(FlaskForm):
    website = StringField('website', validators=[InputRequired("Please input a site address"), Length(min=3, message='Must be at least 3 characters')])

@app.route('/', methods=['GET', 'POST'])
def index():
    lan = obj.current_lan_ip()
    ext = obj.current_wan_ip()
    form = Webchecker()
    if request.method == 'GET':
        return render_template("index.html", form=form, lan=lan, ext=ext)
    if request.method == 'POST':
        if form.is_submitted():
            result = check_website(form.website.data)
        return render_template('webcheck.html', form=form, result=result, lan=lan, ext=ext)

if __name__ == '__main__':
    app.run()
