from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db=SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,nullable=False )
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Token(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    token = db.Column(db.String(100),unique=True,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False)
    ended_at = db.Column(db.DateTime,nullable=False)
    is_active = db.Column(db.Boolean, default=True)

