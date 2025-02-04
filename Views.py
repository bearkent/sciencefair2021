from flask import Blueprint, app, render_template, request, redirect
from flask.helpers import url_for

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import sqlite3

from Craigslist import craigslistGetter

views = Blueprint(__name__, "Views")

# Bootstrap(app)
class ItemForm(FlaskForm):
    date_missed = StringField('When was your item stolen?', validators=[DataRequired()])
    image_link = StringField('Insert a link to the image.', validators=[DataRequired()])
    item_name = StringField('Insert the exact item name.', validators=[DataRequired()])
    submit = SubmitField('Submit')

def get_con():
    return sqlite3.connect("test.db")

def get_row_id(cur, table_name):
    cur.execute(f'''SELECT last_insert_rowid()''')
    return cur.fetchone()[0]

def table_query(cur, table_name, id):
    query = f'''SELECT ROWID, * FROM {table_name} WHERE ROWID == {id}'''
    cur.execute(query)
    vals = cur.fetchone()
    rst = {
        "id": vals[0],
        "date_missed": vals[1],
        "image_link": vals[2],
        "item_name": vals[3]
    }
    return rst

def table_insert(date_missed, image_link, item_name):
    table_name = "items"
    exists = table_exists(table_name)
    
    con = get_con()
    cur=con.cursor()
    if not exists:
        cur.execute(f'''CREATE TABLE {table_name}
            (date_missed text, image_link text, item_name text)''')
        
    cur.execute(f"INSERT INTO {table_name} VALUES ('{date_missed}', '{image_link}', '{item_name}')")
    id = get_row_id(cur, table_name)
    con.commit()
    con.close()

    return id
    
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
		
    con.commit()
    return rst

@views.route("/", methods=["GET", "POST"])
def item_submit():
    
    form = ItemForm()
    message = ""
    date_missed = form.date_missed.data
    image_link = form.image_link.data
    item_name = form.item_name.data 
    ""   

    if request.method == "POST":   
        id = table_insert(date_missed, image_link, item_name)
        return redirect(url_for("Views.id_index", id=id))
    else:
        return render_template("index.html", form=form, message=message)

@views.route("/home_page")
def home_page():
    
    con=get_con()
    cur = con.cursor()
    
    date_misseds = []
    item_links = []
    
    for row in cur.execute('SELECT * FROM items ORDER BY date_missed'):
        return
    return render_template("home_page.html")

@views.route("/print_table")
def print_table():
    con=get_con()
    cur = con.cursor()
    
    rst = "TABLE DATA\n"
    
    for row in cur.execute('SELECT * FROM items ORDER BY date_missed'):
        print(row)
        rst += f"{row}\n"
        
    return rst

@views.route("/print_table2")
def print_table2():
    con=get_con()
    cur = con.cursor()
    date_misseds = []
    item_links = []
    items = []
    
    rst = "TABLE DATA\n"
    
    for row in cur.execute('SELECT ROWID,* FROM items ORDER BY date_missed'):
        items.append(row)
    
    # for item in items:
    #     print(item)
    
    return render_template("home_page.html", len = len(items), items = items)

@views.route('/submission/<id>')
def id_index(id):

    # try:
    #     int(id)
    #     print("valid")
    # except:
    #     print("invalid")
    #     return f"Invalid ID: {id}"
    
    conn = get_con()
    cur = conn.cursor()
    values = table_query(cur, 'items', id)
    items_list = craigslistGetter(values["item_name"], values["date_missed"])

    values["items_list"] = items_list
    print(f"VALUES: {values}")
    return render_template("submit.html", **values)


@views.route("/test")
def test():
    return render_template("test.html")
