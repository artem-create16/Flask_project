from flask import Flask

from .data.config import Configuration
from .data.config import SECRET_KEY

app = Flask(__name__, template_folder='templates')

from .weather.routes import weather_blueprint
from application.weather import routes

from .currency.routes import currency_blueprint


app.config['SECRET_KEY'] = SECRET_KEY

app.config.from_object(Configuration)
app.register_blueprint(weather_blueprint)

app.register_blueprint(currency_blueprint)
