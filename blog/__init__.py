from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='0501d344495cc373a2a73670ca42ae80'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="callLogin"
login_manager.login_message_category="info"

from blog import routes