from flask import Flask, redirect, url_for
from backend.chatbot.controllers import index_blueprint
import os

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.secret_key = os.getenv('APP_SECRET_KEY')


if __name__ == '__main__':
    app.run(debug=True)