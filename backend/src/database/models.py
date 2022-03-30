import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json


database_name = "casting-agency"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

"""
Table Movie
"""
class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(String(250), unique=True, nullable=False)
  genre = db.Column(String(150))
  year = db.Column(String(4), nullable=False)
  rating = db.Column(String(1), nullable=False)

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def formatMovie(self):
    return { 
      'id': self.id,
      'title': self.title,
      'genre': self.genre,
      'year': self.year,
      'rating': self.rating,
    }

"""
Table Actor
"""
class Actor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(String(250), unique=True, nullable= False)
  dateOfBirth = db.Column(String(50), nullable= True)
  nationality = db.Column(String(50), nullable= True)
  #firstAppeared = db.Column(String(4), nullable= False)  ## need to work on the relationship between actors & movies(many to many?)
  netWorth = db.Column(String(50), nullable=True)

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return { 
      'id': self.id,
      'name': self.name,
      'date of birth': self.dateOfBirth,
      'nationality': self.nationality,
      'net worth': self.netWorth,
    }