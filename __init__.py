from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask import send_file
from flask import render_template

comparioAppInstance = Flask(__name__, template_folder='templates')
comparioAppInstance.config.from_object(Config)

db = SQLAlchemy(comparioAppInstance)
migrate = Migrate(comparioAppInstance, db)

login = LoginManager(comparioAppInstance)

from comparioApp import routes, models
