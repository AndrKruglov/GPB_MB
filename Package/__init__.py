from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'qwert'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/minibank_db'
db = SQLAlchemy(app)
#manager = LoginManager(app)

from Package import models, routes
