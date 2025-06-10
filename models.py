from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
 __tablename__ = 'users'

 id=db.Column(db.Integer, primary_key=True)
first_name=db.Column(db.String(50))
last_name=db.Column(db.String(50))
email=db.Column(db.String(120))
username=db.Column(db.String(50))