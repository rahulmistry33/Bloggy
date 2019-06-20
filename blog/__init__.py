from flask_sqlalchemy import SQLAlchemy 
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='0501d344495cc373a2a73670ca42ae80'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)

from blog import routes