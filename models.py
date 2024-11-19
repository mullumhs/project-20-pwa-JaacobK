from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Collum(db.String(100), nullable = False)
    developer = db.Collum(db.String(100))
    publisher = db.Collum(db.String(100))
    realese = db.Collum(db.Int)
    genre = db.Collum(db.String(100))
    image_url = db.Collum(db.String(100))

# Define your database model here
# Example: class Item(db.Model):