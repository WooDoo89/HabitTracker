import os
import urllib
from flask import Flask
from routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def create_app():
    app = Flask(__name__)
    username = urllib.parse.quote_plus(os.environ.get("UNAME"))
    password = urllib.parse.quote_plus(os.environ.get("PASSWORD"))
    client = MongoClient(os.environ.get("MONGODB_URI") % (username, password))
    app.db = client.habit_tracker
    app.register_blueprint(pages)

    return app
