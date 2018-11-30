from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'x1cVx#cx8akxc8#05xa7x97#afVxf2skx91x0e'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes