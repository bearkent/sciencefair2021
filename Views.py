from flask import Blueprint, render_template, request

views = Blueprint(__name__, "Views")

missed_items = []

@views.route("/", methods("GET", "POST"))
def home():
    print(request.form.get("Image Link"))
    missed_items.append((
        request.form.get("date_missed"),
        request.form.get("image_link")
    ))
    return render_template("index.html")

@views.route("/<item>")
def useritem(username):
    return render_template("index.html", name=username)