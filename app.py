from Views import views
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(views, url_prefix="/")

app.config["SECRET_KEY"] = 'jerugejkbgvkjearsbgfvufesa;wqo4kejft2398r'
Bootstrap(app)

# @views.route("/", methods=["GET", "POST"])
# def item_submit():
    
#     print("In /")
    
#     # if request.method == "POST":
#     #     date_missed = request.form["date_missed"],
#     #     image_link = request.form["image_link"]
    
#     #     print(f"DEBUG: {date_missed} {image_link}")
    
#     #     table_insert(date_missed, image_link)
    
#     return "Hey"

    
if __name__ == '__Main__':
    print("HERE")
    app.run(Debug=True)
