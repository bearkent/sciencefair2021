from flask import Flask
from Views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__Main__':
    app.run(Debug=True)
