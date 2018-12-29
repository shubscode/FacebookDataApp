from flask import Flask
from config import Config
from app.facebook_launcher.launcher import create_dictionary

app = Flask(__name__)
app.config.from_object(Config)
create_dictionary()

from app import routes
