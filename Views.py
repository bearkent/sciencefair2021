from flask import Blueprint, app, render_template, request, redirect

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import sqlite3

views = Blueprint(__name__, "Views")

# Bootstrap(app)
class ItemForm(FlaskForm):
    date_missed = StringField('When was your item stolen?', validators=[DataRequired()])
    image_link = StringField('Insert a link to the image here.', validators=[DataRequired()])
    submit = SubmitField('Submit')

def get_con():
    return sqlite3.connect("test.db")

def table_insert(date_missed, image_link):
    
    exists = table_exists("items")
    
    con = get_con()
    cur=con.cursor()
    if not exists:
        cur.execute('''CREATE TABLE items
            (date_missed text, image_link text)''')
    # cur.execute('''CREATE TABLE items
    #         (date_missed text, image_link text)''')
    cur.execute(f"INSERT INTO items VALUES ('{date_missed}', '{image_link}')")
    con.commit()
    con.close()

def table_exists(name):
    con = get_con()
    c = con.cursor()
			
    #get the count of tables with the name
    c.execute(f''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{name}' ''')

    #if the count is 1, then table exists
    if c.fetchone()[0]==1:
        rst = True
        print(f"Table exists: {name}")
    else:
        rst = False
			
    #commit the changes to db			
    con.commit()
    return rst

@views.route("/", methods=["GET", "POST"])
def item_submit():
    
    print("In /")
    
    # if request.method == "POST":
    #     date_missed = request.form["date_missed"],
    #     image_link = request.form["image_link"]
    
    #     print(f"DEBUG: {date_missed} {image_link}")
    
    #     table_insert(date_missed, image_link)
    
    form = ItemForm()
    message = ""
    date_missed = form.date_missed.data
    image_link = form.image_link.data    

    # redirect("/home_page")
    return render_template("index.html", form=form, message=message)

# @views.route("/home_page")
# def home_page():
#     for row in cur.execute('SELECT * FROM items ORDER BY date_missed'):
#         print(row)
#     return render_template("home_page.html")

@views.route("/print_table")
def print_table():
    con=get_con()
    cur = con.cursor()
    
    rst = "TABLE DATA\n"
    
    for row in cur.execute('SELECT * FROM items ORDER BY date_missed'):
        print(row)
        rst += f"{row}\n"
        
    return rst