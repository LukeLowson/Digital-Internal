from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique= True)
    firstName = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    notes = db.relationship('Note')
    music = db.relationship('Music', backref='user', passive_deletes=True)
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    