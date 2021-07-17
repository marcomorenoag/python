from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Required only to enforce FK constaints to SQLite
from sqlalchemy import event
from sqlalchemy.engine import Engine


# Initialize our Flask app, behind scenes Flask use a WSGI to connect Python App with the server
app = Flask(__name__)

# Connect to a local testing SQLITE database for learning purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlitedb.file'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ! EXTRA CONFIG TO SQLITE TO USE FK CONSTRAINTS
# Configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, 'connect')
def _set_sqlite_pragma(dbapi_connection, connection_record):
  if isinstance(dbapi_connection, SQLite3Connection):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreing_keys=ON;')
    cursor.close()

# Instance of DataBase (connect ORM with our Flask app)
db = SQLAlchemy(app)
now = datetime.now() # date values when updating tables

# ! DATABASE
# To connect and query database we use Flask-SQLAlchemy extension that is an ORM
# * Models
class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50))
  address = db.Column(db.String(200))
  phone = db.Column(db.String(50))
  posts = db.relationship('BlogPost')

class BlogPost(db.Model):
  __tablename__ = 'blog_post'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(50))
  body = db.Column(db.String(200))
  date = db.Column(db.Date)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)