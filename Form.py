from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app import app

Bootstrap(app)

class ItemForm(FlaskForm):
    date_missed = StringField('When was your item stolen?', validators=[DataRequired()])
    image_link = StringField('Insert a link to the image here.', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
def Form():
    
    form = ItemForm()
    message = ""
    
    if form.validate.submit():
        date = form.date_missed.data
        link = form.image_link.data