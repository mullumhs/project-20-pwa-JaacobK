from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    developer = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    realese = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    image_url = db.Column(db.String(100))

# Define your database model here
# Example: class Item(db.Model):