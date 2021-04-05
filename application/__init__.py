from flask import Flask
from config import Configuration

app = Flask(__name__, template_folder='templates')

import os


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config.from_object(Configuration)


from application import views