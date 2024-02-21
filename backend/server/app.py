from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Profile, Post, Comment, Message, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite3'
# db = SQLAlchemy(app)

migrate = Migrate(app, db)

db.init_app(app)

